# SPDX-License-Identifier: MIT
"""Placeholder registry, parsing, and substitution shared by generate.py and check_library.py.

A placeholder is [NAME] or [NAME, e.g., example text]. Example text may itself contain
placeholders, so the parser matches brackets by depth rather than with a single regex.
"""
import glob
import os
import re
import tomllib

CONTENT_DIRS = ("policies", "standards", "runbooks", "templates", "addenda", "client-facing")
REGISTRY_FILE = "placeholders.toml"
# Described in the customization guide's prose, so excluded from its table.
STANDARD_PLACEHOLDERS = {"ORGANIZATION_NAME", "EFFECTIVE_DATE", "POLICY_OWNER", "EXECUTIVE_SPONSOR"}
PHASES = {"adoption", "use"}
# The closing attribution line every document carries, word for word, so that the
# generator can find and remove it reliably.
ATTRIBUTION_LINE = ("*Adopted from `github.com/pslorenz/security-policy-templates` (CC BY 4.0). "
                    "Organizations adopting this document for their own use may remove this line.*")
GUIDE_TABLE_HEADER = "| Placeholder | Used in | What to supply |\n|---|---|---|\n"

_START = re.compile(r"\[([A-Z][A-Z0-9_]+)(\]|, )")
_DOC_ID = re.compile(r"^((?:POL|STD|RUN|TPL|ADD|GUI|PLY)-[A-Z]+-\d{3})")


class Placeholder:
    """One outermost placeholder occurrence in a piece of text."""

    __slots__ = ("start", "end", "name", "example", "eg")

    def __init__(self, start, end, name, example, eg=False):
        self.start, self.end, self.name, self.example, self.eg = start, end, name, example, eg

    def __repr__(self):
        return f"Placeholder({self.name!r}, example={self.example!r})"


def find_placeholders(text):
    """Return the outermost placeholders in text, in order.

    Square brackets that do not start with an uppercase NAME followed by ']' or ', '
    (Markdown links, checkboxes, prose) are ignored.
    """
    found, i = [], 0
    while True:
        m = _START.search(text, i)
        if not m:
            return found
        name, closer = m.group(1), m.group(2)
        if closer == "]" and text.startswith("(", m.end()):  # a Markdown link, not a placeholder
            i = m.end()
            continue
        if closer == "]":
            found.append(Placeholder(m.start(), m.end(), name, None))
            i = m.end()
            continue
        depth, j = 1, m.end()
        while j < len(text) and depth:
            if text[j] == "[":
                depth += 1
            elif text[j] == "]":
                depth -= 1
            j += 1
        if depth:  # unbalanced; treat as plain text
            i = m.end()
            continue
        example = text[m.end():j - 1]
        eg = example.startswith("e.g., ")
        if eg:
            example = example[len("e.g., "):]
        found.append(Placeholder(m.start(), j, name, example, eg))
        i = j


def names_in(text):
    """Every placeholder name in text, including those nested inside example text."""
    names = set()
    for p in find_placeholders(text):
        names.add(p.name)
        if p.example:
            names |= names_in(p.example)
    return names


def substitute(text, resolve):
    """Replace placeholders using resolve(name, example) -> str or None.

    None keeps the placeholder, with any placeholders inside its example text still
    substituted. Returns the new text.
    """
    out, last = [], 0
    for p in find_placeholders(text):
        out.append(text[last:p.start])
        inner = substitute(p.example, resolve) if p.example else p.example
        value = resolve(p.name, inner)
        if value is not None:
            out.append(value)
        elif p.example is None:
            out.append(f"[{p.name}]")
        else:
            sep = ", e.g., " if p.eg else ", "
            out.append(f"[{p.name}{sep}{inner}]")
        last = p.end
    out.append(text[last:])
    return "".join(out)


def load_registry(root="."):
    with open(os.path.join(root, REGISTRY_FILE), "rb") as fh:
        return tomllib.load(fh)


def content_files(root="."):
    files = []
    for d in CONTENT_DIRS:
        files += glob.glob(os.path.join(root, d, "*.md"))
    return sorted(files)


def document_label(path):
    """Document ID for numbered documents, a readable title for client-facing explainers."""
    base = os.path.basename(path)
    m = _DOC_ID.match(base)
    if m:
        return m.group(1)
    words = os.path.splitext(base)[0].split("-")
    return " ".join(w.upper() if w in {"nhi", "ai"} else w.capitalize() for w in words)


def usage(root="."):
    """Map each placeholder name to the set of document labels that use it."""
    used = {}
    for f in content_files(root):
        with open(f, encoding="utf-8") as fh:
            text = fh.read()
        for name in names_in(text):
            used.setdefault(name, set()).add(document_label(f))
    return used


def render_guide_table(registry, used):
    """The placeholder table for docs/customization-guide.md, generated from the registry."""
    rows, groups = [], {}
    for name, entry in registry.items():
        if name in STANDARD_PLACEHOLDERS or name not in used:
            continue
        group = entry.get("group")
        if group:
            groups.setdefault(group, []).append(name)
        else:
            docs = ", ".join(sorted(used[name]))
            rows.append((name.lower(), f"| `[{name}]` | {docs} | {entry['description']} |"))
    for members in groups.values():
        members.sort(key=str.lower)
        docs = ", ".join(sorted(set().union(*(used[n] for n in members))))
        desc = registry[members[0]]["description"]
        cells = ", ".join(f"`[{n}]`" for n in members)
        rows.append((members[0].lower(), f"| {cells} | {docs} | {desc} |"))
    rows.sort()
    return GUIDE_TABLE_HEADER + "\n".join(r for _, r in rows)


def guide_table_span(guide_text):
    """(start, end) of the placeholder table in the customization guide."""
    start = guide_text.index(GUIDE_TABLE_HEADER)
    end = guide_text.index("\n\n", start)
    return start, end


def collect_examples(root="."):
    """The first example text given anywhere in the library for each placeholder."""
    examples = {}

    def walk(text):
        for p in find_placeholders(text):
            if p.example:
                examples.setdefault(p.name, p.example)
                walk(p.example)

    for f in content_files(root):
        with open(f, encoding="utf-8") as fh:
            walk(fh.read())
    return examples


def strip_attribution(text):
    """Remove the attribution line, and a closing rule left with nothing after it."""
    lines = [line for line in text.split("\n") if line.strip() != ATTRIBUTION_LINE]
    while lines and not lines[-1].strip():
        lines.pop()
    if lines and lines[-1].strip() == "---":
        lines.pop()
        while lines and not lines[-1].strip():
            lines.pop()
    return "\n".join(lines) + "\n"
