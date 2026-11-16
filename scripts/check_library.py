#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Consistency and voice checks for the security-policy-templates library.

Run from the repository root:  python3 scripts/check_library.py
Exits non-zero if any check fails. Each failure names the file, the line
where one applies, and the rule that was broken.
"""
import glob
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import intake  # noqa: E402
import placeholders as P  # noqa: E402

ID_TYPES = "POL|STD|RUN|TPL|ADD|GUI|PLY"
ID_RE = re.compile(r"\b(?:%s)-[A-Z]+-\d{3}\b" % ID_TYPES)
FILE_RE = re.compile(r"^(((?:%s)-([A-Z]+))-(\d{3}))-[a-z0-9-]+\.md$" % ID_TYPES)

# Files that discuss the rules rather than follow them.
VOICE_EXEMPT = {"CHANGELOG.md", "CONTRIBUTING.md", os.path.join("docs", "style-guide.md")}
# CHANGELOG records retired IDs on purpose.
REFERENCE_EXEMPT = {"CHANGELOG.md"}

BANNED_WORDS = [
    "leverage", "leverages", "leveraging", "synergy", "synergies", "robust",
    "seamless", "seamlessly", "best-in-class", "world-class", "delve",
    "very", "really", "extremely", "incredibly",
]
BANNED_PHRASES = ["it is important to note", "it should be observed", "in today's"]
BRITISH = re.compile(r"\b\w*(organis|behaviour|programme|prioritis|licence\b|analyse\b|centre\b|favour)\w*", re.I)
# Product names that must not appear as examples inside placeholders.
PLACEHOLDER_PRODUCTS = [
    "Microsoft Defender", "Sentinel", "Intune", "CrowdStrike", "SentinelOne", "Huntress",
    "Okta", "1Password", "Bitwarden", "Keeper", "Splunk", "Tenable", "Qualys", "Rapid7",
    "Fortinet", "Sophos", "SonicWall", "Ubiquiti", "Cisco", "Umbrella", "Cloudflare",
    "Tailscale", "Twingate", "Zscaler", "Jamf", "Mandiant", "Kroll", "Unit 42",
    "SecurityScorecard", "BitSight", "Blumira", "Elastic", "ChatGPT", "Copilot",
    "Claude", "Gemini", "Slack", "Teams", "Veeam", "Datto", "Proofpoint", "Mimecast",
]
PLACEHOLDER_RE = re.compile(r"\[[A-Z][A-Z0-9_]+,\s*e\.g\.,[^\]]*\]")

failures = []


def fail(path, line, rule, detail=""):
    loc = f"{path}:{line}" if line else path
    failures.append(f"{loc}: {rule}" + (f" ({detail})" if detail else ""))


def md_files():
    return sorted(f for f in glob.glob("**/*.md", recursive=True)
                  if not f.startswith((".git", "node_modules", "build", "deliver")))


def headings(text):
    return set(re.findall(r"^#{2,5} (\d+(?:\.\d+)*)[ .]", text, re.M))


def main():
    files = md_files()
    texts = {f: open(f, encoding="utf-8").read() for f in files}

    # Identified documents, ID consistency, and sequences.
    docs, seq = {}, defaultdict(list)
    for f, text in texts.items():
        m = FILE_RE.match(os.path.basename(f))
        if not m:
            if ID_RE.match(os.path.basename(f)):
                fail(f, None, "filename does not follow ID-kebab-title.md")
            continue
        doc_id, prefix, num = m.group(1), m.group(2), int(m.group(4))
        if doc_id in docs:
            fail(f, None, "duplicate document ID", doc_id)
        docs[doc_id] = f
        seq[prefix].append(num)
        if not re.search(r"^# %s: " % re.escape(doc_id), text, re.M):
            fail(f, 1, "H1 does not start with the document ID", doc_id)
        if f"| **Document ID** | {doc_id} |" not in text:
            fail(f, None, "metadata Document ID does not match filename", doc_id)
        if P.ATTRIBUTION_LINE not in text.split("\n"):
            fail(f, None, "closing attribution line missing or not worded exactly as placeholders.ATTRIBUTION_LINE")
    for prefix, nums in sorted(seq.items()):
        if sorted(nums) != list(range(1, len(nums) + 1)):
            fail(prefix, None, "numbers are not sequential from 001", ", ".join(f"{n:03d}" for n in sorted(nums)))

    for f in files:
        if f.startswith("client-facing" + os.sep) and P.ATTRIBUTION_LINE not in texts[f].split("\n"):
            fail(f, None, "closing attribution line missing or not worded exactly as placeholders.ATTRIBUTION_LINE")

    # Cross-references and section references.
    sections = {d: headings(texts[p]) for d, p in docs.items()}
    for f, text in texts.items():
        if f in REFERENCE_EXEMPT:
            continue
        own = FILE_RE.match(os.path.basename(f))
        own_id = own.group(1) if own else None
        for n, line in enumerate(text.splitlines(), 1):
            for ref in ID_RE.findall(line):
                if ref not in docs:
                    fail(f, n, "reference to a document that does not exist", ref)
            for ref, sec in re.findall(r"\b((?:%s)-[A-Z]+-\d{3}) Sections? (\d+(?:\.\d+)*)" % ID_TYPES, line):
                if ref in sections and sec not in sections[ref]:
                    fail(f, n, "section does not exist in target", f"{ref} Section {sec}")
            for ref, lst in re.findall(r"\b((?:%s)-[A-Z]+-\d{3}) Sections ((?:\d+(?:\.\d+)*(?:, | and |, and )?)+)" % ID_TYPES, line):
                for sec in re.findall(r"\d+(?:\.\d+)+", lst):
                    if ref in sections and sec not in sections[ref]:
                        fail(f, n, "section does not exist in target", f"{ref} Section {sec}")

    # Voice.
    word_re = re.compile(r"\b(%s)\b" % "|".join(map(re.escape, BANNED_WORDS)), re.I)
    for f, text in texts.items():
        in_code = False
        for n, line in enumerate(text.splitlines(), 1):
            if line.strip().startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            if "\u2014" in line or "\u2013" in line:
                fail(f, n, "em-dash or en-dash")
            if f in VOICE_EXEMPT:
                continue
            if re.search(r"(?<!\")\bshall\b(?!\.?\")", line, re.I):
                fail(f, n, "uses 'shall'")
            if re.search(r"(^|[.!?] )(And|But) ", line):
                fail(f, n, "sentence starts with And or But")
            m = word_re.search(line)
            if m:
                fail(f, n, "banned word", m.group(1))
            for p in BANNED_PHRASES:
                if p in line.lower():
                    fail(f, n, "banned phrase", p)
            m = BRITISH.search(line)
            if m:
                fail(f, n, "British spelling", m.group(0))
            for ph in PLACEHOLDER_RE.findall(line):
                for prod in PLACEHOLDER_PRODUCTS:
                    if re.search(r"\b%s\b" % re.escape(prod), ph):
                        fail(f, n, "product name in placeholder example", prod)

    # Placeholder registry: every placeholder registered, every registration used,
    # and the customization guide's table generated from the registry.
    registry = P.load_registry()
    used = P.usage()
    for name, entry in registry.items():
        if entry.get("phase") not in P.PHASES:
            fail(P.REGISTRY_FILE, None, "phase must be 'adoption' or 'use'", name)
        if not entry.get("description"):
            fail(P.REGISTRY_FILE, None, "missing description", name)
        if name not in used:
            fail(P.REGISTRY_FILE, None, "registered placeholder no longer used in any document", name)
        if entry.get("phase") == "adoption" and "default" not in entry:
            if entry.get("section") not in intake.SECTIONS or not entry.get("question"):
                fail(P.REGISTRY_FILE, None, "adoption placeholder needs a question and a valid section", name)
    for name, labels in sorted(used.items()):
        if name not in registry:
            fail(", ".join(sorted(labels)), None, "placeholder not registered in placeholders.toml", name)
    guide_path = os.path.join("docs", "customization-guide.md")
    guide = texts[guide_path]
    start, end = P.guide_table_span(guide)
    if guide[start:end] != P.render_guide_table(registry, used):
        fail(guide_path, None, "placeholder table is out of date",
             "run: python3 scripts/generate.py --update-guide")

    with open(intake.QUESTIONNAIRE, encoding="utf-8") as fh:
        if fh.read() != intake.render():
            fail(intake.QUESTIONNAIRE, None, "questionnaire is out of date",
                 "run: python3 scripts/generate.py --update-guide")

    if failures:
        print(f"{len(failures)} problem(s) found:\n")
        print("\n".join(failures))
        return 1
    print(f"All checks passed: {len(docs)} numbered documents, {len(files)} Markdown files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
