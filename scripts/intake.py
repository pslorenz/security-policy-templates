#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Intake questionnaire: render it from the registry, and turn a filled-in copy into a client config.

Usage, from the repository root:

    cp docs/intake-questionnaire.md clients/acme-intake.md      # then fill in the Answer column
    python3 scripts/intake.py clients/acme-intake.md --out clients/acme.toml
    python3 scripts/generate.py clients/acme.toml

The questionnaire itself is generated from placeholders.toml by
`python3 scripts/generate.py --update-guide`; edit the registry, not the questionnaire.
"""
import argparse
import datetime
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import placeholders as P  # noqa: E402

QUESTIONNAIRE = os.path.join("docs", "intake-questionnaire.md")

# Ordered sections of Part 2: key -> (title, who usually answers).
SECTIONS = {
    "organization": ("Your organization", "the owner or executive sponsor"),
    "roles": ("Leadership and roles", "the owner or executive sponsor"),
    "people": ("People and policies", "operations or HR"),
    "finance": ("Finance and payments", "finance"),
    "it": ("IT and security tools", "the IT lead or IT provider"),
    "monitoring": ("Monitoring and logging", "the IT lead or IT provider"),
    "recovery": ("Backup, recovery, and continuity", "the owner, with the IT lead or IT provider"),
    "incident": ("Incidents and outside help", "the owner or executive sponsor"),
    "cmmc": ("Defense contracts with CUI (skip unless you handle CUI)", "the owner, with the IT lead"),
    "explainers": ("Business owner explainers (optional)", "whoever presents the program to leadership"),
}

# Part 1: the five scoping questions from docs/adoption-guide.md, plus document statuses.
SCOPE_QUESTIONS = [
    ("scope.office_network", "Do you have an office network or on-premises servers?", "yes / no"),
    ("scope.self_hosted_internet_services",
     "Do you run anything reachable from the internet yourself, such as a VPN or remote desktop gateway, "
     "a file transfer server, or a hosted site with logins?", "yes / no"),
    ("scope.writes_code", "Does anyone write code for the organization, including scripts and automations? "
     "If so, what kind?", "none / scripts / internal / internet-facing"),
    ("scope.regulated_data", "Do you handle any of these regulated kinds of data?",
     "none, or any of: cui, health, payment-card, nydfs"),
    ("scope.it_provider", "Does an outside provider run your IT or security?", "yes / no"),
    ("documents", "Are there any documents you are not adopting yet, or not adopting at all? "
     "List each as ID: Planned or ID: Not adopted, separated by semicolons.",
     "for example, STD-DC-001: Planned; TPL-LOG-002: Not adopted"),
]

_DOC_PRIORITY = ("policies", "standards", "runbooks", "templates", "client-facing", "addenda")
# Asked first within their sections; everything else follows alphabetically.
_FIRST = ["ORGANIZATION_NAME", "EFFECTIVE_DATE", "EXECUTIVE_SPONSOR", "POLICY_OWNER", "CONTINUITY_LEAD",
          "CONTINUITY_DEPUTY"]


def _cell(text):
    """Make text safe for one Markdown table cell."""
    return " ".join(text.replace("|", "/").split())


def _clean(text):
    return text.replace("**", "").replace("*", "").strip()


def usage_sentence(name, files):
    """The first sentence or table cell in the library that uses this placeholder,
    with the placeholder shown as ___."""
    def resolver(n, example):
        if n == name:
            return "___"
        if n == "ORGANIZATION_NAME":
            return "your organization"
        return "..."

    for f in files:
        with open(f, encoding="utf-8") as fh:
            for line in fh:
                if f"[{name}" not in line:
                    continue
                line = re.sub(r"\*\*[^*]+\*\*\s*", "", line, count=1) if line.startswith("**") else line
                if line.lstrip().startswith("|"):
                    parts = [c for c in line.strip().strip("|").split("|") if f"[{name}" in c]
                    chunk = parts[0] if parts else line
                else:
                    sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z\[*])", line.strip())
                    chunk = next((s for s in sentences if f"[{name}" in s), line)
                text = _clean(P.substitute(chunk, resolver))
                if len(text) > 220:
                    i = text.find("___")
                    text = "..." + text[max(0, i - 110): i + 110] + "..."
                return text
    return ""


def ordered_files(root="."):
    """Library documents in the order used to find each placeholder's usage sentence."""
    return sorted(P.content_files(root),
                  key=lambda f: (_DOC_PRIORITY.index(os.path.relpath(f, root).split(os.sep)[0]), f))


def section_keys(registry, section):
    return sorted((k for k, v in registry.items() if v.get("section") == section),
                  key=lambda k: (_FIRST.index(k) if k in _FIRST else len(_FIRST), k))


def usage_text(key, registry, files):
    used = usage_sentence(key, files)
    if len(used.replace("___", "").strip(" .")) < 12:  # a bare table cell says nothing useful
        used = registry[key]["description"]
    return used


def example_text(key, examples):
    return P.substitute(examples.get(key, ""),
                        lambda n, e: "your organization" if n == "ORGANIZATION_NAME" else None)


def render(root="."):
    registry = P.load_registry(root)
    files = ordered_files(root)
    examples = P.collect_examples(root)
    lines = [
        "# Intake Questionnaire",
        "",
        "*The decisions needed to customize the library for one organization, in plain language.*",
        "",
        "---",
        "",
        "## How to use this questionnaire",
        "",
        "Copy this file for each organization, fill in the Answer column, and turn it into a configuration "
        "file for the generator:",
        "",
        "```bash",
        "cp docs/intake-questionnaire.md clients/acme-intake.md",
        "python3 scripts/intake.py clients/acme-intake.md --out clients/acme.toml",
        "python3 scripts/generate.py clients/acme.toml",
        "```",
        "",
        "Each section says who usually answers it. Most organizations need about an hour with the owner and "
        "an hour with whoever runs IT.",
        "",
        "**Answers go into the documents word for word.** The \"How your answer is used\" column shows a "
        "sentence from the library with ___ where the answer goes. Write an answer that completes that "
        "sentence naturally. The Example column shows the kind of answer that fits.",
        "",
        "**Leave a question blank if you do not know yet.** The generator lists every unanswered question "
        "for the documents you are adopting, so nothing is missed. Questions in sections that do not apply "
        "to you, such as the CUI section, can stay blank.",
        "",
        "This questionnaire is generated from `placeholders.toml`. To change a question, edit the registry "
        "and run `python3 scripts/generate.py --update-guide`.",
        "",
        "---",
        "",
        "## Part 1: Scope",
        "",
        "These answers decide which documents apply. The adoption guide (`docs/adoption-guide.md`) explains "
        "each one.",
        "",
        "| Key | Question | Choices | Answer |",
        "|---|---|---|---|",
    ]
    lines += [f"| `{k}` | {_cell(q)} | {_cell(c)} | |" for k, q, c in SCOPE_QUESTIONS]
    lines += ["", "## Part 2: Details", ""]
    for n, (key, (title, who)) in enumerate(SECTIONS.items(), 1):
        names = section_keys(registry, key)
        if not names:
            continue
        lines += [f"### 2.{n} {title}", "", f"*Usually answered by {who}.*", "",
                  "| Key | Question | How your answer is used | Example | Answer |",
                  "|---|---|---|---|---|"]
        for k in names:
            used = usage_text(k, registry, files)
            example = example_text(k, examples)
            lines.append(f"| `{k}` | {_cell(registry[k]['question'])} | {_cell(used)} | {_cell(example)} | |")
        lines.append("")
    lines += ["---", "",
              "*Adopted from `github.com/pslorenz/security-policy-templates`, distributed under "
              "Creative Commons Attribution 4.0.*", ""]
    return "\n".join(lines)


def update_questionnaire(root="."):
    with open(os.path.join(root, QUESTIONNAIRE), "w", encoding="utf-8") as fh:
        fh.write(render(root))


class IntakeError(Exception):
    pass


def _answers_from_markdown(path):
    answers = {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r"^\| `([A-Za-z_.]+)` \|(.*)\|\s*$", line)
            if m:
                answer = m.group(2).split("|")[-1].strip()
                if answer:
                    answers[m.group(1)] = answer
    return answers


def _answers_from_xlsx(path):
    try:
        import openpyxl
    except ImportError:
        raise IntakeError("reading an Excel questionnaire needs openpyxl: pip install openpyxl")
    wb = openpyxl.load_workbook(path, data_only=True)
    ws = wb["Questions"] if "Questions" in wb.sheetnames else wb.active
    header = [str(c.value).strip() if c.value is not None else "" for c in ws[1]]
    if "Key" not in header or "Answer" not in header:
        raise IntakeError(f"{path}: the questions sheet needs Key and Answer columns")
    key_col, answer_col = header.index("Key"), header.index("Answer")
    answers = {}
    for row in ws.iter_rows(min_row=2, values_only=True):
        key, value = row[key_col], row[answer_col]
        if not key or value is None or str(value).strip() == "":
            continue
        if isinstance(value, (datetime.datetime, datetime.date)):
            value = value.date().isoformat() if isinstance(value, datetime.datetime) else value.isoformat()
        elif isinstance(value, float) and value.is_integer():
            value = str(int(value))
        answers[str(key).strip()] = " ".join(str(value).split())
    return answers


def parse(path):
    """Read a filled-in questionnaire (Markdown or Excel) and return a config dict for generate.py."""
    answers = _answers_from_xlsx(path) if path.lower().endswith(".xlsx") else _answers_from_markdown(path)

    config = {"generation": {"use_examples": False}, "scope": {}, "documents": {}, "values": {}}
    errors = []
    for key, answer in answers.items():
        if key in ("scope.office_network", "scope.self_hosted_internet_services", "scope.it_provider"):
            if answer.lower() not in ("yes", "no"):
                errors.append(f"{key}: answer yes or no")
            else:
                config["scope"][key.split(".")[1]] = answer.lower() == "yes"
        elif key == "scope.writes_code":
            config["scope"]["writes_code"] = answer.lower()
        elif key == "scope.regulated_data":
            items = [i.strip().lower() for i in re.split(r"[,;]", answer) if i.strip()]
            config["scope"]["regulated_data"] = [] if items == ["none"] else items
        elif key == "documents":
            for item in re.split(r";|<br>", answer):
                if not item.strip():
                    continue
                doc, _, status = item.partition(":")
                if not status.strip():
                    errors.append(f"documents: '{item.strip()}' should be ID: status")
                else:
                    config["documents"][doc.strip()] = status.strip()
        else:
            config["values"][key] = answer
    if errors:
        raise IntakeError("\n".join(errors))
    return config


def to_toml(config, source):
    def string(v):
        return '"' + v.replace("\\", "\\\\").replace('"', '\\"') + '"'

    def value(v):
        if isinstance(v, bool):
            return "true" if v else "false"
        if isinstance(v, list):
            return "[" + ", ".join(string(x) for x in v) + "]"
        return string(v)

    lines = [f"# Generated {datetime.date.today().isoformat()} from {source} by scripts/intake.py.",
             "# Review it, then run: python3 scripts/generate.py <this file>", ""]
    for table in ("generation", "scope", "documents", "values"):
        lines.append(f"[{table}]")
        for k, v in config[table].items():
            key = f'"{k}"' if "-" in k else k
            lines.append(f"{key} = {value(v)}")
        lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Turn a filled-in intake questionnaire into a client config.")
    parser.add_argument("questionnaire", help="filled-in questionnaire: a copy of docs/intake-questionnaire.md, "
                                              "or the Excel version from export.py --questionnaire")
    parser.add_argument("--out", required=True, help="config file to write (TOML)")
    args = parser.parse_args()
    try:
        config = parse(args.questionnaire)
    except IntakeError as exc:
        print(f"Problems in {args.questionnaire}:\n{exc}", file=sys.stderr)
        return 1
    if os.path.dirname(args.out):
        os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(to_toml(config, args.questionnaire))
    print(f"Wrote {args.out} with {len(config['values'])} answer(s). Next: python3 scripts/generate.py {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
