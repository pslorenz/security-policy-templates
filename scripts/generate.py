#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Generate an organization's customized copy of the library from a client config.

Usage, from the repository root:

    python3 scripts/generate.py clients/acme.toml               # writes build/acme/
    python3 scripts/generate.py clients/acme.toml --out out/acme
    python3 scripts/generate.py --update-guide                  # regenerate the guide's placeholder table and the questionnaire

The client config is a TOML file with [scope], [documents], [values], and an optional
[generation] table. See examples/clients/sample-remote-firm.toml.

The script never modifies the library itself (except the guide table with --update-guide).
It exits non-zero if the config has errors or an adopted document is left with an unfilled
adoption-time placeholder.
"""
import argparse
import datetime
import os
import re
import shutil
import subprocess
import sys
import tomllib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import intake  # noqa: E402
import placeholders as P  # noqa: E402

STATUS_ADOPTED, STATUS_PLANNED, STATUS_NOT_ADOPTED = "Adopted", "Planned", "Not adopted"
SCOPE_KEYS = {
    "office_network": bool,
    "self_hosted_internet_services": bool,
    "writes_code": {"none", "scripts", "internal", "internet-facing"},
    "regulated_data": {"cui", "health", "payment-card", "nydfs"},
    "it_provider": bool,
}
TESTING_TIERS = {"Baseline", "Standard", "Expanded"}
DEV_LEVELS = {
    "scripts": "Adopted at the scripts and automations level",
    "internal": "Adopted at the internal applications level",
    "internet-facing": "Adopted at the internet-facing applications level",
}


class ConfigError(Exception):
    pass


def format_value(value, key):
    if isinstance(value, bool):
        raise ConfigError(f"[values] {key}: use text, not true/false")
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, datetime.date):
        return value.isoformat()
    if isinstance(value, list):
        items = [format_value(v, key) for v in value]
        if len(items) <= 2:
            return " and ".join(items)
        return ", ".join(items[:-1]) + ", and " + items[-1]
    if isinstance(value, str):
        # Collapse whitespace so multi-line values cannot break a table row.
        return " ".join(value.split())
    raise ConfigError(f"[values] {key}: unsupported value type {type(value).__name__}")


def document_ids(root):
    ids = {}
    for f in P.content_files(root):
        label = P.document_label(f)
        if re.match(r"^[A-Z]{3}-[A-Z]+-\d{3}$", label):
            ids[label] = f
    return ids


def resolve_statuses(config, ids, warnings):
    """Adoption status for every numbered document."""
    scope = config.get("scope", {})
    given = config.get("documents", {})
    for doc in given:
        if doc not in ids:
            raise ConfigError(f"[documents] {doc}: no such document in the library")
    statuses = {}
    for doc in ids:
        if doc in given:
            status = given[doc]
            if not (status in (STATUS_PLANNED, STATUS_NOT_ADOPTED) or status.startswith(STATUS_ADOPTED)):
                raise ConfigError(f"[documents] {doc}: status must be 'Adopted...', 'Planned', or 'Not adopted'")
        elif doc.startswith("ADD-"):
            status = STATUS_NOT_ADOPTED  # addenda apply only when chosen
        elif doc == "POL-DEV-001":
            level = scope.get("writes_code", "none")
            status = DEV_LEVELS.get(level, STATUS_NOT_ADOPTED)
        else:
            status = STATUS_ADOPTED
        statuses[doc] = status

    # Consistency warnings between the scope answers and the statuses.
    adopted = lambda d: statuses[d].startswith(STATUS_ADOPTED)  # noqa: E731
    if "cui" in scope.get("regulated_data", []) and not adopted("ADD-CMMC-001"):
        warnings.append("scope says CUI is handled, but ADD-CMMC-001 is not adopted")
    if scope.get("writes_code", "none") == "none" and adopted("POL-DEV-001"):
        warnings.append("scope says no code is written, but POL-DEV-001 is adopted")
    tier = config.get("values", {}).get("TESTING_TIER")
    if scope.get("self_hosted_internet_services") and tier == "Baseline":
        warnings.append("scope says internet-facing services are self-hosted, but TESTING_TIER is Baseline "
                        "(STD-VM-001 Section 3.1 calls for Standard)")
    return statuses


def validate_config(config, registry):
    errors = []
    for key in config:
        if key not in {"scope", "documents", "values", "generation", "export"}:
            errors.append(f"unknown table [{key}]")
    for key, value in config.get("generation", {}).items():
        if key not in {"use_examples", "keep_attribution"}:
            errors.append(f"[generation] {key}: unknown option")
        elif not isinstance(value, bool):
            errors.append(f"[generation] {key}: must be true or false")
    for key, value in config.get("scope", {}).items():
        rule = SCOPE_KEYS.get(key)
        if rule is None:
            errors.append(f"[scope] {key}: unknown key")
        elif rule is bool and not isinstance(value, bool):
            errors.append(f"[scope] {key}: must be true or false")
        elif isinstance(rule, set):
            values = value if isinstance(value, list) else [value]
            bad = [v for v in values if v not in rule]
            if bad:
                errors.append(f"[scope] {key}: {bad} not in {sorted(rule)}")
    for key in config.get("values", {}):
        entry = registry.get(key)
        if entry is None:
            errors.append(f"[values] {key}: not a registered placeholder (check placeholders.toml for the spelling)")
        elif entry["phase"] == "use":
            errors.append(f"[values] {key}: use-time placeholder; it is filled when the template is used, not at adoption")
    tier = config.get("values", {}).get("TESTING_TIER")
    if tier is not None and tier not in TESTING_TIERS:
        errors.append(f"[values] TESTING_TIER: must be one of {sorted(TESTING_TIERS)}")
    if errors:
        raise ConfigError("\n".join(errors))


def status_banner(status, org):
    if status == STATUS_NOT_ADOPTED:
        return (f"*Status at {org}: Not adopted. This document is retained for reference because "
                f"adopted documents refer to it.*")
    if status == STATUS_PLANNED:
        return f"*Status at {org}: Planned. Not yet in effect.*"
    return None


def suite_status_cell(template_cell, status):
    if status == STATUS_ADOPTED:
        return template_cell
    if status.startswith(STATUS_ADOPTED):
        detail = status[len(STATUS_ADOPTED):].strip()
        return f"Active ({detail})" if detail else "Active"
    return status


def rewrite_suite_table(text, statuses):
    """Set the Status column of the POL-GOV-001 Section 3.7 suite table from the config."""
    def fix(m):
        doc, title, cell = m.group(1), m.group(2), m.group(3)
        if doc not in statuses:
            return m.group(0)
        return f"| {doc} | {title} | {suite_status_cell(cell, statuses[doc])} |"
    return re.sub(r"^\| ((?:POL|STD)-[A-Z]+-\d{3}) \| ([^|]+?) \| ([^|]+?) \|$", fix, text, flags=re.M)


def git_revision(root):
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=root, capture_output=True,
                              text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown (not a git checkout)"


def generate(config_path, out_dir, root="."):
    registry = P.load_registry(root)
    with open(config_path, "rb") as fh:
        config = tomllib.load(fh)
    validate_config(config, registry)

    values = {k: format_value(v, k) for k, v in config.get("values", {}).items()}
    for name, entry in registry.items():
        if entry.get("phase") == "adoption" and "default" in entry:
            values.setdefault(name, entry["default"])
    use_examples = config.get("generation", {}).get("use_examples", False)
    keep_attribution = config.get("generation", {}).get("keep_attribution", False)
    org = values.get("ORGANIZATION_NAME", "[ORGANIZATION_NAME]")
    warnings, errors, examples_used = [], [], {}
    ids = document_ids(root)
    statuses = resolve_statuses(config, ids, warnings)
    library_examples = P.collect_examples(root) if use_examples else {}

    def resolver(name, example):
        if registry.get(name, {}).get("phase") != "adoption":
            return None
        if name in values:
            return values[name]
        # In draft mode, use the example given here, or the one given for the same
        # placeholder elsewhere in the library.
        example = example or library_examples.get(name)
        if use_examples and example:
            examples_used.setdefault(name, example)
            return example
        return None

    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    for f in P.content_files(root):
        rel = os.path.relpath(f, root)
        label = P.document_label(f)
        with open(f, encoding="utf-8") as fh:
            text = fh.read()
        text = P.substitute(text, resolver)
        if not keep_attribution:
            text = P.strip_attribution(text)
        if label == "POL-GOV-001":
            text = rewrite_suite_table(text, statuses)
        status = statuses.get(label, STATUS_ADOPTED)
        banner = status_banner(status, org)
        if use_examples:
            draft = "*DRAFT: generated with example values for review. Not in effect.*"
            banner = f"{draft}\n\n{banner}" if banner else draft
        if banner:
            text = re.sub(r"^(# .+\n)", lambda m: m.group(1) + "\n" + banner + "\n", text, count=1, flags=re.M)

        # Anything adoption-time still unfilled is an error in adopted documents.
        left = sorted(n for n in P.names_in(text) if registry.get(n, {}).get("phase") == "adoption")
        if left:
            msg = f"{rel}: unfilled {', '.join(left)}"
            if status == STATUS_NOT_ADOPTED:
                pass
            elif use_examples or rel.startswith("client-facing") or status == STATUS_PLANNED:
                warnings.append(msg)
            else:
                errors.append(msg)

        dest = os.path.join(out_dir, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as fh:
            fh.write(text)

    shutil.copy(os.path.join(root, "LICENSE"), os.path.join(out_dir, "LICENSE"))
    write_notice(out_dir, org)
    write_report(out_dir, config_path, org, statuses, examples_used, warnings, errors, root, use_examples,
                 keep_attribution)
    return errors, warnings


def write_notice(out_dir, org):
    text = f"""NOTICE

The documents in this folder were prepared for {org} and are adapted from
Security Policy Templates by P. Steven Lorenz
(https://github.com/pslorenz/security-policy-templates), licensed under the
Creative Commons Attribution 4.0 International License (CC BY 4.0). They have
been modified from the originals.

{org} may use these documents for its own purposes without crediting the
source in the documents themselves.

Anyone who redistributes these documents, or a collection derived from them,
to others must credit the source as CC BY 4.0 requires. Keeping this notice
with the collection is one way to do so. See LICENSE.
"""
    with open(os.path.join(out_dir, "NOTICE"), "w", encoding="utf-8") as fh:
        fh.write(text)


def write_report(out_dir, config_path, org, statuses, examples_used, warnings, errors, root, draft=False,
                 keep_attribution=False):
    lines = [
        f"# Generation Report: {org}" + (" (DRAFT)" if draft else ""),
        "",
    ]
    if draft:
        lines += ["This is a draft generated with `use_examples` on. Placeholders without a configured value "
                  "were filled with the library's example text where one exists, and unfilled placeholders are "
                  "reported as warnings rather than errors. Do not put this copy into effect.", ""]
    lines += [
        f"Generated {datetime.date.today().isoformat()} from `{config_path}` using library revision "
        f"{git_revision(root)}.",
        "",
        "## Document status",
        "",
        "| Document | Status |",
        "|---|---|",
    ]
    lines += [f"| {d} | {s} |" for d, s in sorted(statuses.items())]
    lines += ["", "## Attribution", "",
              "The closing attribution line was kept in every document (`keep_attribution` is on)."
              if keep_attribution else
              "The closing attribution line was removed from every document. Credit is given once, in the "
              "NOTICE file in this folder."]
    if examples_used:
        lines += ["", "## Example text used as values", "",
                  "These placeholders had no value in the config and were filled with the library's "
                  "example text because `use_examples` is on. Review each one.", ""]
        lines += [f"- `{n}`: {e}" for n, e in sorted(examples_used.items())]
    for title, items in (("Warnings", warnings), ("Errors", errors)):
        if items:
            lines += ["", f"## {title}", ""] + [f"- {i}" for i in items]
    lines.append("")
    with open(os.path.join(out_dir, "GENERATION_REPORT.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


def update_guide(root="."):
    path = os.path.join(root, "docs", "customization-guide.md")
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    start, end = P.guide_table_span(text)
    table = P.render_guide_table(P.load_registry(root), P.usage(root))
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text[:start] + table + text[end:])
    intake.update_questionnaire(root)
    print(f"Updated the placeholder table in {path} and the questionnaire in {intake.QUESTIONNAIRE}.")


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("config", nargs="?", help="client config (TOML)")
    parser.add_argument("--out", help="output directory (default: build/<config name>)")
    parser.add_argument("--update-guide", action="store_true",
                        help="regenerate the customization guide's placeholder table and the intake questionnaire "
                             "from placeholders.toml")
    args = parser.parse_args()

    if args.update_guide:
        update_guide()
        return 0
    if not args.config:
        parser.error("a config file is required unless --update-guide is given")

    out = args.out or os.path.join("build", os.path.splitext(os.path.basename(args.config))[0])
    try:
        errors, warnings = generate(args.config, out)
    except ConfigError as exc:
        print(f"Config errors in {args.config}:\n{exc}", file=sys.stderr)
        return 1
    for w in warnings:
        print(f"warning: {w}", file=sys.stderr)
    for e in errors:
        print(f"error: {e}", file=sys.stderr)
    if errors:
        print(f"\n{len(errors)} adopted document(s) have unfilled placeholders. Output written to {out} "
              f"for review, but it is not ready to use.", file=sys.stderr)
        return 1
    print(f"Generated {out} ({len(warnings)} warning(s)). See {out}/GENERATION_REPORT.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
