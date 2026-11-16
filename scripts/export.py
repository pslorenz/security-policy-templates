#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Export a generated library to Word and Excel, and the intake questionnaire to Excel.

Usage, from the repository root:

    python3 scripts/export.py build/acme --config clients/acme.toml --out deliver/acme
    python3 scripts/export.py --questionnaire deliver/intake-questionnaire.xlsx

Requirements: Pandoc 3.x on the PATH, and the Python packages python-docx and openpyxl
(pip install python-docx openpyxl). The generator itself needs none of these.

Policies, standards, runbooks, addenda, and client-facing explainers become Word documents.
Templates become an Excel workbook (one sheet per table, plus a Read Me sheet) and a Word
copy for the narrative and the forms. PDFs are left to the reader: open the Word file and
export after review.
"""
import argparse
import copy
import os
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import placeholders as P  # noqa: E402

DEFAULTS = {"font": "Arial", "primary_color": "1F4E79", "prepared_by": "", "logo": "",
            "include_not_adopted": False}
WORD_DIRS = {"policies": "Policies", "standards": "Standards", "runbooks": "Runbooks",
             "addenda": "Addenda", "client-facing": "Client-Facing", "templates": "Templates"}
APPROVAL_TYPES = ("POL", "STD", "ADD")
NOT_ADOPTED_MARK = "Not adopted. This document is retained for reference"
CHOICE_RE = re.compile(r"^[A-Za-z][A-Za-z0-9 ]*( / [A-Za-z0-9][A-Za-z0-9 ]*)+$")


def require(module):
    try:
        return __import__(module)
    except ImportError:
        sys.exit(f"export.py needs the Python package '{module}'. Install it with: pip install {module.replace('docx', 'python-docx')}")


def check_pandoc():
    if not shutil.which("pandoc"):
        sys.exit("export.py needs Pandoc 3.x on the PATH: https://pandoc.org/installing.html")


# ---------------------------------------------------------------- shared parsing

def doc_info(text, path):
    """ID, title, version, and classification from a library document."""
    m = re.search(r"^# (.+)$", text, re.M)
    h1 = m.group(1).strip() if m else os.path.basename(path)
    doc_id, _, title = h1.partition(": ")
    if not re.match(r"^[A-Z]{3}-[A-Z]+-\d{3}$", doc_id):
        doc_id, title = "", h1

    def meta(label):
        mm = re.search(r"^\| \*\*%s\*\* \| (.+?) \|$" % re.escape(label), text, re.M)
        return mm.group(1).strip() if mm else ""
    return {"id": doc_id, "title": title, "version": meta("Version") or "1.0",
            "classification": meta("Classification"), "approver": meta("Approver")}


def clean_cell(text):
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"(?<!\w)\*(.+?)\*(?!\w)", r"\1", text)
    return text.replace("`", "").replace("<br>", "\n").strip()


def markdown_tables(text):
    """Yield (heading, rows) for each table, rows being lists of cell strings.
    The first table (the metadata block) is skipped."""
    heading, tables, block = "", [], []
    in_code = False
    for line in text.splitlines() + [""]:
        if line.startswith("```"):
            in_code = not in_code
        if in_code:
            continue
        if line.startswith("|"):
            block.append(line)
            continue
        if block:
            rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in block]
            rows = [r for r in rows if not all(re.fullmatch(r":?-{3,}:?", c) for c in r)]
            tables.append((heading, rows))
            block = []
        m = re.match(r"^#{2,4} (.+)$", line) or re.match(r"^\*\*([^*]+)\*\*$", line.strip())
        if m:
            heading = m.group(1).strip()
    return tables[1:]


# ---------------------------------------------------------------- Word

def build_reference(opts, workdir):
    """A reference document carrying the fonts, colors, and table style."""
    docx = require("docx")
    from docx.shared import Pt, RGBColor
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement

    path = os.path.join(workdir, "reference.docx")
    subprocess.run(["pandoc", "-o", path, "--print-default-data-file", "reference.docx"], check=True)
    d = docx.Document(path)
    # Look styles up by their stored name; python-docx's own lookup lowercases built-in
    # names ("heading 1"), which does not match Pandoc's reference document.
    by_name = {}
    for s in d.styles:
        n = s.element.find(qn("w:name"))
        if n is not None:
            by_name[n.get(qn("w:val")).lower()] = s

    class _Styles:
        def __getitem__(self, key):
            return by_name[key.lower()]
    styles = _Styles()
    color = RGBColor.from_string(opts["primary_color"].lstrip("#").upper())
    for name in ("Normal", "Body Text", "First Paragraph", "Compact", "Title", "Subtitle",
                 "Heading 1", "Heading 2", "Heading 3", "Heading 4", "Table"):
        try:
            style = styles[name]
        except KeyError:
            continue
        style.font.name = opts["font"]
        rpr = style.element.get_or_add_rPr()
        fonts = rpr.find(qn("w:rFonts"))
        if fonts is None:
            fonts = OxmlElement("w:rFonts")
            rpr.append(fonts)
        for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
            fonts.set(qn(attr), opts["font"])
        for attr in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
            if fonts.get(qn(attr)) is not None:
                del fonts.attrib[qn(attr)]
        if name.startswith("Heading") or name == "Title":
            style.font.color.rgb = color
            style.font.bold = True
    for name, size in (("Normal", 10.5), ("Body Text", 10.5), ("Compact", 10), ("Title", 22),
                       ("Heading 1", 16), ("Heading 2", 13), ("Heading 3", 11.5), ("Heading 4", 11)):
        try:
            styles[name].font.size = Pt(size)
        except KeyError:
            pass

    # Table style: thin borders and a shaded header row.
    try:
        table_style = styles["Table"].element
        tblpr = table_style.find(qn("w:tblPr"))
        if tblpr is None:
            tblpr = OxmlElement("w:tblPr")
            table_style.append(tblpr)
        borders = OxmlElement("w:tblBorders")
        for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
            b = OxmlElement(f"w:{edge}")
            b.set(qn("w:val"), "single")
            b.set(qn("w:sz"), "4")
            b.set(qn("w:color"), "A6A6A6")
            borders.append(b)
        for old in tblpr.findall(qn("w:tblBorders")):
            tblpr.remove(old)
        tblpr.append(borders)
    except KeyError:
        pass
    d.save(path)
    return path


def _field(paragraph, instr):
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), instr)
    r = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), "16")
    col = OxmlElement("w:color")
    col.set(qn("w:val"), "595959")
    rpr.extend([col, sz])
    r.append(rpr)
    t = OxmlElement("w:t")
    t.text = "1"
    r.append(t)
    fld.append(r)
    paragraph._p.append(fld)


def finish_word(path, info, org, opts):
    """Header, footer, and header-row shading on a Pandoc-built document."""
    docx = require("docx")
    from docx.shared import Pt, RGBColor, Inches
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn

    d = docx.Document(path)
    grey = RGBColor(0x59, 0x59, 0x59)
    for section in d.sections:
        section.left_margin = section.right_margin = Inches(1)
        hp = section.header.paragraphs[0]
        hp.text = ""
        if opts["logo"]:
            hp.add_run().add_picture(opts["logo"], height=Inches(0.35))
            hp.add_run("    ")
        label = " ".join(x for x in (info["id"], info["title"]) if x)
        run = hp.add_run(f"{org}  |  {label}" if org else label)
        run.font.size, run.font.color.rgb, run.font.name = Pt(8.5), grey, opts["font"]

        fp = section.footer.paragraphs[0]
        fp.text = ""
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        bits = [b for b in (info["classification"] and f"Classification: {info['classification']}",
                            f"Version {info['version']}", opts["prepared_by"] and f"Prepared by {opts['prepared_by']}") if b]
        run = fp.add_run("  |  ".join(bits) + "  |  Page ")
        run.font.size, run.font.color.rgb, run.font.name = Pt(8), grey, opts["font"]
        _field(fp, "PAGE")
        run = fp.add_run(" of ")
        run.font.size, run.font.color.rgb = Pt(8), grey
        _field(fp, "NUMPAGES")

    fill = opts["primary_color"].lstrip("#").upper()
    for table in d.tables:
        if not table.rows:
            continue
        header = table.rows[0]
        if not any(c.text.strip() for c in header.cells):
            # Label/value forms have an empty Markdown header row; drop it.
            header._tr.getparent().remove(header._tr)
            continue
        for cell in header.cells:
            tcpr = cell._tc.get_or_add_tcPr()
            shd = OxmlElement("w:shd")
            shd.set(qn("w:val"), "clear")
            shd.set(qn("w:color"), "auto")
            shd.set(qn("w:fill"), fill)
            tcpr.append(shd)
            for p in cell.paragraphs:
                for r in p.runs:
                    r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                    r.font.bold = True
        trpr = header._tr.get_or_add_trPr()
        rep = OxmlElement("w:tblHeader")
        trpr.append(rep)
    d.save(path)


def approval_block(info, org):
    approver = info["approver"] or "Executive sponsor"
    return ("\n\n## Approval\n\n"
            f"Approved for {org or 'the organization'}.\n\n"
            "| | |\n|---|---|\n"
            f"| **Approved by** | {approver} |\n| **Signature** | |\n| **Date** | |\n")


def to_word(src, dest, reference, info, org, opts, transform=None):
    with open(src, encoding="utf-8") as fh:
        text = fh.read()
    if transform:
        text = transform(text)
    if info["id"][:3] in APPROVAL_TYPES:
        # Before the closing rule and attribution line, so the attribution stays last.
        cut = text.rstrip().rfind("\n---\n")
        if cut == -1:
            text = text.rstrip() + approval_block(info, org)
        else:
            text = text[:cut].rstrip() + approval_block(info, org) + text[cut:]
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as tmp:
        tmp.write(text)
    try:
        subprocess.run(["pandoc", tmp.name, "-f", "gfm", "-o", dest, f"--reference-doc={reference}",
                        "--metadata", "lang=en-US"], check=True)
    finally:
        os.unlink(tmp.name)
    finish_word(dest, info, org, opts)


# ---------------------------------------------------------------- Excel

def _xl_styles(opts):
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    thin = Side(style="thin", color="BFBFBF")
    return {
        "font": Font(name=opts["font"], size=10),
        "bold": Font(name=opts["font"], size=10, bold=True),
        "header_font": Font(name=opts["font"], size=10, bold=True, color="FFFFFF"),
        "title": Font(name=opts["font"], size=14, bold=True, color=opts["primary_color"].lstrip("#")),
        "header_fill": PatternFill("solid", fgColor=opts["primary_color"].lstrip("#")),
        "input_fill": PatternFill("solid", fgColor="FFF8DC"),
        "label_fill": PatternFill("solid", fgColor="F2F2F2"),
        "border": Border(left=thin, right=thin, top=thin, bottom=thin),
        "wrap": Alignment(wrap_text=True, vertical="top"),
    }


def _print_setup(ws, header_row=True):
    """Landscape, one page wide, header row repeated, so a sheet prints usably."""
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    if header_row:
        ws.print_title_rows = "1:1"


def _choices(header, seed):
    """Dropdown options from a header like 'Outcome (Pass / Fix / Remove)' or a seed cell 'Yes / No'."""
    m = re.search(r"\(([^()]+ / [^()]+)\)\s*$", header)
    for candidate in (seed, m.group(1) if m else ""):
        if candidate and CHOICE_RE.match(candidate.strip()):
            return [c.strip() for c in candidate.split(" / ")]
    return None


def _sheet_name(heading, used):
    name = re.sub(r"^\d+(\.\d+)*\.?\s*", "", heading) or "Sheet"
    name = re.sub(r"[\[\]:*?/\\]", "", name)[:31].strip()
    base, n = name, 2
    while name.lower() in used:
        name = f"{base[:28]} {n}"
        n += 1
    used.add(name.lower())
    return name


def template_workbook(src, dest, info, org, opts):
    openpyxl = require("openpyxl")
    from openpyxl.utils import get_column_letter
    from openpyxl.worksheet.datavalidation import DataValidation

    with open(src, encoding="utf-8") as fh:
        text = fh.read()
    st = _xl_styles(opts)
    wb = openpyxl.Workbook()
    readme = wb.active
    readme.title = "Read Me"
    how = ""
    m = re.search(r"^## How to use this template\n\n(.+?)\n\n", text, re.M | re.S)
    if m:
        how = clean_cell(m.group(1))
    rows = [(f"{info['id']}: {info['title']}", st["title"]), (org, st["bold"]), ("", None),
            (how, st["font"]), ("", None),
            ("How this workbook works", st["bold"]),
            ("Each table in the template is a sheet. Shaded cells are for your entries; columns with a "
             "fixed set of answers have a dropdown. The first rows of each sheet are the template's "
             "example rows: replace them with real entries.", st["font"]),
            ("The Word copy of this template holds the instructions, checks, and outcome rules.", st["font"]),
            ("", None),
            ("Adopted from github.com/pslorenz/security-policy-templates, distributed under "
             "Creative Commons Attribution 4.0.", st["font"])]
    for i, (value, font) in enumerate(rows, 1):
        c = readme.cell(row=i, column=1, value=value)
        if font:
            c.font = font
        c.alignment = st["wrap"]
    readme.column_dimensions["A"].width = 100

    used = {"read me"}
    sheet_names = []
    for heading, table in markdown_tables(text):
        if not table:
            sheet_names.append(None)
            continue
        ws = wb.create_sheet(_sheet_name(heading, used))
        sheet_names.append(ws.title)
        header = [clean_cell(c) for c in table[0]]
        form = not any(header)  # a label/value form such as "Review Details"
        body = table[1:] if not form else table[1:]
        start = 1
        if not form:
            for col, value in enumerate(header, 1):
                c = ws.cell(row=1, column=col, value=value)
                c.font, c.fill, c.border, c.alignment = st["header_font"], st["header_fill"], st["border"], st["wrap"]
            start = 2
        for r_off, row in enumerate(body):
            for col, raw in enumerate(row, 1):
                value = clean_cell(raw)
                choice = not form and col <= len(header) and _choices(header[col - 1], value)
                c = ws.cell(row=start + r_off, column=col, value=None if choice and value and CHOICE_RE.match(value) else (value or None))
                c.font, c.border, c.alignment = st["font"], st["border"], st["wrap"]
                if form:
                    if col == 1:
                        c.font, c.fill = st["bold"], st["label_fill"]
                    else:
                        c.fill = st["input_fill"]
                elif not value or (choice and CHOICE_RE.match(value or "")):
                    c.fill = st["input_fill"]
        if not form:
            last = start + len(body) + 24  # room for entries
            for row in range(start + len(body), last + 1):
                for col in range(1, len(header) + 1):
                    c = ws.cell(row=row, column=col)
                    c.border, c.fill, c.font, c.alignment = st["border"], st["input_fill"], st["font"], st["wrap"]
            for col, h in enumerate(header, 1):
                seed = clean_cell(body[0][col - 1]) if body and col <= len(body[0]) else ""
                options = _choices(h, seed)
                if options:
                    dv = DataValidation(type="list", formula1='"' + ",".join(options) + '"', allow_blank=True)
                    ws.add_data_validation(dv)
                    letter = get_column_letter(col)
                    dv.add(f"{letter}{start}:{letter}{last}")
            ws.freeze_panes = "A2"
            ws.auto_filter.ref = f"A1:{get_column_letter(len(header))}{last}"
            _print_setup(ws)
            for col, h in enumerate(header, 1):
                ws.column_dimensions[get_column_letter(col)].width = max(12, min(40, len(h) + 4))
        else:
            ws.column_dimensions["A"].width = 45
            ws.column_dimensions["B"].width = 60
            _print_setup(ws, header_row=False)
    wb.save(dest)
    return sheet_names


WIDE_TABLE_COLUMNS = 6


def point_wide_tables_to_workbook(text, sheet_names, workbook_name):
    """Replace tables too wide for a portrait page with a pointer to their Excel sheet.
    The first table (the metadata block) is never replaced."""
    out, block, index, in_code = [], [], -1, False

    def flush():
        nonlocal index
        if not block:
            return
        index += 1
        columns = block[0].strip().strip("|").count("|") + 1
        sheet = sheet_names[index - 1] if 0 < index <= len(sheet_names) else None
        if index > 0 and columns > WIDE_TABLE_COLUMNS and sheet:
            out.append(f'*This table is in the Excel workbook {workbook_name}, on the sheet "{sheet}".*')
        else:
            out.extend(block)
        block.clear()

    for line in text.splitlines():
        if line.startswith("```"):
            in_code = not in_code
        if not in_code and line.startswith("|"):
            block.append(line)
            continue
        flush()
        out.append(line)
    flush()
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------- questionnaire

def questionnaire_workbook(dest, opts):
    openpyxl = require("openpyxl")
    from openpyxl.worksheet.datavalidation import DataValidation
    import intake

    st = _xl_styles(opts)
    registry = P.load_registry()
    wb = openpyxl.Workbook()
    readme = wb.active
    readme.title = "Read Me"
    lines = [("Intake Questionnaire", st["title"]),
             ("The decisions needed to customize the security policy library for one organization.", st["font"]),
             ("", None),
             ("Fill in the Answer column on the Questions sheet. Each row says who usually answers it. "
              "Answers go into the documents word for word: the 'How your answer is used' column shows the "
              "sentence your answer completes, with ___ where it goes. Leave a question blank if you do not "
              "know yet; the generator lists anything still needed.", st["font"]),
             ("", None),
             ("When it is complete, convert it with: python3 scripts/intake.py questionnaire.xlsx --out client.toml",
              st["font"]),
             ("", None),
             ("Adopted from github.com/pslorenz/security-policy-templates, distributed under "
              "Creative Commons Attribution 4.0.", st["font"])]
    for i, (value, font) in enumerate(lines, 1):
        c = readme.cell(row=i, column=1, value=value)
        if font:
            c.font = font
        c.alignment = st["wrap"]
    readme.column_dimensions["A"].width = 100

    ws = wb.create_sheet("Questions")
    headers = ["Key", "Section", "Usually answered by", "Question", "How your answer is used", "Example", "Answer"]
    widths = [22, 24, 24, 48, 48, 30, 45]
    for col, (h, w) in enumerate(zip(headers, widths), 1):
        c = ws.cell(row=1, column=col, value=h)
        c.font, c.fill, c.border, c.alignment = st["header_font"], st["header_fill"], st["border"], st["wrap"]
        ws.column_dimensions[openpyxl.utils.get_column_letter(col)].width = w

    rows = []
    for key, question, choices in intake.SCOPE_QUESTIONS:
        label = "Format" if choices.startswith("for example") else "Choices"
        rows.append((key, "Scope", "the owner or executive sponsor", question, f"{label}: {choices}", "", choices))
    files = intake.ordered_files()
    examples = P.collect_examples()
    for section, (title, who) in intake.SECTIONS.items():
        for k in intake.section_keys(registry, section):
            rows.append((k, title, who, registry[k]["question"], intake.usage_text(k, registry, files),
                         intake.example_text(k, examples), None))
    for r, (key, section, who, question, used, example, choices) in enumerate(rows, 2):
        for col, value in enumerate((key, section, who, question, used, example, None), 1):
            c = ws.cell(row=r, column=col, value=value)
            c.font, c.border, c.alignment = st["font"], st["border"], st["wrap"]
        ws.cell(row=r, column=1).font = openpyxl.styles.Font(name=opts["font"], size=9, color="808080")
        ws.cell(row=r, column=7).fill = st["input_fill"]
        if choices and " / " in choices and "," not in choices:
            dv = DataValidation(type="list", formula1='"' + ",".join(c.strip() for c in choices.split("/")) + '"',
                                allow_blank=True)
            ws.add_data_validation(dv)
            dv.add(f"G{r}")
    ws.freeze_panes = "D2"
    ws.auto_filter.ref = f"A1:G{len(rows) + 1}"
    _print_setup(ws)
    wb.save(dest)


# ---------------------------------------------------------------- main

def load_options(config_path):
    opts = dict(DEFAULTS)
    org = ""
    if config_path:
        with open(config_path, "rb") as fh:
            config = tomllib.load(fh)
        unknown = set(config.get("export", {})) - set(DEFAULTS)
        if unknown:
            sys.exit(f"[export] unknown option(s): {', '.join(sorted(unknown))}")
        opts.update(config.get("export", {}))
        org = str(config.get("values", {}).get("ORGANIZATION_NAME", ""))
    if opts["logo"] and not os.path.exists(opts["logo"]):
        sys.exit(f"[export] logo not found: {opts['logo']}")
    opts["primary_color"] = opts["primary_color"].lstrip("#")
    return opts, org


def export_library(src, out, opts, org):
    check_pandoc()
    require("docx")
    require("openpyxl")
    if os.path.exists(out):
        shutil.rmtree(out)
    with tempfile.TemporaryDirectory() as work:
        reference = build_reference(opts, work)
        count = {"docx": 0, "xlsx": 0, "skipped": 0}
        for sub, folder in WORD_DIRS.items():
            for path in sorted(P.content_files(src)):
                if os.path.relpath(path, src).split(os.sep)[0] != sub:
                    continue
                with open(path, encoding="utf-8") as fh:
                    text = fh.read()
                if NOT_ADOPTED_MARK in text and not opts["include_not_adopted"]:
                    count["skipped"] += 1
                    continue
                info = doc_info(text, path)
                name = os.path.splitext(os.path.basename(path))[0]
                os.makedirs(os.path.join(out, folder), exist_ok=True)
                transform = None
                if sub == "templates":
                    sheets = template_workbook(path, os.path.join(out, folder, name + ".xlsx"), info, org, opts)
                    count["xlsx"] += 1
                    transform = lambda t, s=sheets, n=name: point_wide_tables_to_workbook(t, s, n + ".xlsx")  # noqa: E731
                to_word(path, os.path.join(out, folder, name + ".docx"), reference, info, org, opts, transform)
                count["docx"] += 1
    for extra in ("LICENSE", "NOTICE", "GENERATION_REPORT.md"):
        if os.path.exists(os.path.join(src, extra)):
            shutil.copy(os.path.join(src, extra), os.path.join(out, extra))
    return count


def main():
    parser = argparse.ArgumentParser(description="Export a generated library to Word and Excel.")
    parser.add_argument("source", nargs="?", help="generated library folder (output of generate.py)")
    parser.add_argument("--config", help="client config, for [export] options and the organization name")
    parser.add_argument("--out", help="output folder (default: deliver/<source folder name>)")
    parser.add_argument("--questionnaire", metavar="XLSX", help="write the intake questionnaire as Excel and exit")
    args = parser.parse_args()

    opts, org = load_options(args.config)
    if args.questionnaire:
        require("openpyxl")
        if os.path.dirname(args.questionnaire):
            os.makedirs(os.path.dirname(args.questionnaire), exist_ok=True)
        questionnaire_workbook(args.questionnaire, opts)
        print(f"Wrote {args.questionnaire}.")
        return 0
    if not args.source:
        parser.error("a source folder is required unless --questionnaire is given")
    if not os.path.exists(os.path.join(args.source, "policies")):
        parser.error(f"{args.source} does not look like generate.py output (no policies/ folder)")
    out = args.out or os.path.join("deliver", os.path.basename(os.path.normpath(args.source)))
    count = export_library(args.source, out, opts, org)
    print(f"Exported {count['docx']} Word document(s) and {count['xlsx']} workbook(s) to {out}"
          + (f"; skipped {count['skipped']} not-adopted document(s)" if count["skipped"] else "") + ".")
    return 0


if __name__ == "__main__":
    sys.exit(main())
