# SPDX-License-Identifier: MIT
"""Tests for the placeholder parser and the generator. Run from the repository root:

    python3 -m unittest discover -s tests
"""
import os
import sys
import tempfile
import tomllib
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import generate  # noqa: E402
import placeholders as P  # noqa: E402

SAMPLE = os.path.join(ROOT, "examples", "clients", "sample-remote-firm.toml")


class ParserTests(unittest.TestCase):
    def test_simple_and_example_placeholders(self):
        found = P.find_placeholders("A [ORG_NAME] and [TOOLS, e.g., two tools] here.")
        self.assertEqual([p.name for p in found], ["ORG_NAME", "TOOLS"])
        self.assertEqual(found[1].example, "two tools")

    def test_nested_placeholder_in_example(self):
        text = '[RISK_STATEMENT, e.g., "[ORG_NAME] accepts low risk."]'
        found = P.find_placeholders(text)
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].end, len(text))
        self.assertEqual(P.names_in(text), {"RISK_STATEMENT", "ORG_NAME"})

    def test_ignores_links_checkboxes_and_prose(self):
        text = "See [the guide](docs/x.md), - [ ] item, [README](x), and [lowercase text]."
        self.assertEqual(P.find_placeholders(text), [])

    def test_substitute_keeps_unresolved_and_fills_nested(self):
        text = '[RISK_STATEMENT, e.g., "[ORG_NAME] accepts."] [DATE]'
        out = P.substitute(text, lambda n, e: "Acme" if n == "ORG_NAME" else None)
        self.assertEqual(out, '[RISK_STATEMENT, e.g., "Acme accepts."] [DATE]')

    def test_strip_attribution(self):
        text = "Body.\n\n---\n\n*Issued under authority.*\n\n" + P.ATTRIBUTION_LINE + "\n"
        self.assertEqual(P.strip_attribution(text), "Body.\n\n---\n\n*Issued under authority.*\n")
        text = "Body.\n\n---\n\n" + P.ATTRIBUTION_LINE + "\n"
        self.assertEqual(P.strip_attribution(text), "Body.\n")

    def test_substitute_replaces_example_text_entirely(self):
        out = P.substitute("Tools: [TOOLS, e.g., a, b, and c].", lambda n, e: "our EDR")
        self.assertEqual(out, "Tools: our EDR.")


class GeneratorTests(unittest.TestCase):
    def setUp(self):
        self.cwd = os.getcwd()
        os.chdir(ROOT)
        self.registry = P.load_registry()

    def tearDown(self):
        os.chdir(self.cwd)

    def test_sample_config_generates_cleanly(self):
        with tempfile.TemporaryDirectory() as out:
            errors, _ = generate.generate(SAMPLE, os.path.join(out, "client"))
            self.assertEqual(errors, [])
            gov = open(os.path.join(out, "client", "policies",
                                    "POL-GOV-001-information-security-policy.md")).read()
            self.assertIn("Harbor & Pine Advisory LLC", gov)
            self.assertNotIn("[ORGANIZATION_NAME]", gov)

    def test_attribution_removed_by_default_and_kept_on_request(self):
        with tempfile.TemporaryDirectory() as out:
            generate.generate(SAMPLE, os.path.join(out, "a"))
            gov = open(os.path.join(out, "a", "policies", "POL-GOV-001-information-security-policy.md")).read()
            self.assertNotIn("Adopted from", gov)
            self.assertIn("issued under the authority", gov)
            self.assertTrue(os.path.exists(os.path.join(out, "a", "NOTICE")))
        with open(SAMPLE, "rb") as fh:
            config = tomllib.load(fh)
        config["generation"]["keep_attribution"] = True
        with tempfile.TemporaryDirectory() as out:
            path = os.path.join(out, "c.toml")
            with open(path, "w") as fh:
                fh.write(to_toml(config))
            generate.generate(path, os.path.join(out, "k"))
            gov = open(os.path.join(out, "k", "policies", "POL-GOV-001-information-security-policy.md")).read()
            self.assertIn(P.ATTRIBUTION_LINE, gov)

    def test_use_time_placeholders_survive(self):
        with tempfile.TemporaryDirectory() as out:
            generate.generate(SAMPLE, os.path.join(out, "client"))
            tpl = open(os.path.join(out, "client", "templates",
                                    "TPL-IAM-001-quarterly-nhi-access-review.md")).read()
            self.assertIn("[QUARTER_YEAR]", tpl)
            self.assertIn("[NHI_ID]", tpl)

    def test_missing_value_is_an_error(self):
        with open(SAMPLE, "rb") as fh:
            config = tomllib.load(fh)
        del config["values"]["CRITICAL_RTO"]
        errors = self._generate_with(config)
        self.assertTrue(any("CRITICAL_RTO" in e for e in errors))

    def test_use_examples_fills_missing_values(self):
        with open(SAMPLE, "rb") as fh:
            config = tomllib.load(fh)
        del config["values"]["CRITICAL_RTO"]
        config["generation"]["use_examples"] = True
        self.assertEqual(self._generate_with(config), [])

    def test_unknown_and_use_time_keys_are_rejected(self):
        for key in ("ORGANISATION_NAME", "QUARTER_YEAR"):
            with self.assertRaises(generate.ConfigError):
                generate.validate_config({"values": {key: "x"}}, self.registry)

    def _generate_with(self, config):
        with tempfile.TemporaryDirectory() as out:
            path = os.path.join(out, "client.toml")
            with open(path, "w") as fh:
                fh.write(to_toml(config))
            errors, _ = generate.generate(path, os.path.join(out, "client"))
            return errors


def to_toml(config):
    """Minimal TOML writer for the test configs (tables of scalars, lists, and dates)."""
    def fmt(v):
        if isinstance(v, bool):
            return "true" if v else "false"
        if isinstance(v, (int, float)):
            return str(v)
        if isinstance(v, list):
            return "[" + ", ".join(fmt(x) for x in v) + "]"
        if hasattr(v, "isoformat"):
            return v.isoformat()
        return '"' + str(v).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'
    lines = []
    for table, entries in config.items():
        lines.append(f"[{table}]")
        lines += [f'"{k}" = {fmt(v)}' for k, v in entries.items()]
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    unittest.main()


class IntakeTests(unittest.TestCase):
    def setUp(self):
        self.cwd = os.getcwd()
        os.chdir(ROOT)
        import intake
        self.intake = intake

    def tearDown(self):
        os.chdir(self.cwd)

    def test_questionnaire_round_trip(self):
        """Filling the questionnaire with the sample config's answers reproduces that config."""
        with open(SAMPLE, "rb") as fh:
            sample = tomllib.load(fh)
        answers = {f"scope.{k}": ("yes" if v is True else "no" if v is False else
                                  ", ".join(v) if isinstance(v, list) else v)
                   for k, v in sample["scope"].items()}
        answers["scope.regulated_data"] = answers["scope.regulated_data"] or "none"
        answers["documents"] = "; ".join(f"{k}: {v}" for k, v in sample["documents"].items())
        for k, v in sample["values"].items():
            answers[k] = " ".join(str(v).split())
        filled = []
        for line in self.intake.render().splitlines():
            for key, answer in answers.items():
                if line.startswith(f"| `{key}` |") and line.endswith("| |"):
                    line = line[:-2] + f" {answer} |"
            filled.append(line)
        with tempfile.TemporaryDirectory() as out:
            path = os.path.join(out, "filled.md")
            with open(path, "w") as fh:
                fh.write("\n".join(filled))
            config = self.intake.parse(path)
            self.assertEqual(config["scope"], sample["scope"])
            self.assertEqual(config["documents"], sample["documents"])
            asked = {k for k, v in P.load_registry().items() if "question" in v}
            for k, v in sample["values"].items():
                if k in asked:
                    self.assertEqual(config["values"][k], " ".join(str(v).split()), k)
            toml_path = os.path.join(out, "client.toml")
            with open(toml_path, "w") as fh:
                fh.write(self.intake.to_toml(config, "filled.md"))
            errors, _ = generate.generate(toml_path, os.path.join(out, "client"))
            self.assertEqual(errors, [])

    def test_bad_scope_answer_is_reported(self):
        with tempfile.TemporaryDirectory() as out:
            path = os.path.join(out, "filled.md")
            with open(path, "w") as fh:
                fh.write("| `scope.office_network` | Q | yes / no | maybe |\n")
            with self.assertRaises(self.intake.IntakeError):
                self.intake.parse(path)


def _export_tools_available():
    import shutil
    try:
        import docx  # noqa: F401
        import openpyxl  # noqa: F401
    except ImportError:
        return False
    return shutil.which("pandoc") is not None


@unittest.skipUnless(_export_tools_available(), "Pandoc, python-docx, and openpyxl are needed for export tests")
class ExportTests(unittest.TestCase):
    def setUp(self):
        self.cwd = os.getcwd()
        os.chdir(ROOT)
        import export
        import intake
        self.export, self.intake = export, intake

    def tearDown(self):
        os.chdir(self.cwd)

    def test_sample_exports_word_and_excel(self):
        import openpyxl
        with tempfile.TemporaryDirectory() as out:
            build, deliver = os.path.join(out, "build"), os.path.join(out, "deliver")
            generate.generate(SAMPLE, build)
            opts, org = self.export.load_options(SAMPLE)
            count = self.export.export_library(build, deliver, opts, org)
            self.assertGreater(count["docx"], 30)
            with open(SAMPLE, "rb") as fh:
                skipped = [d for d, s in tomllib.load(fh)["documents"].items()
                           if d.startswith("TPL-") and s == "Not adopted"]
            self.assertEqual(count["xlsx"], len(os.listdir(os.path.join(ROOT, "templates"))) - len(skipped))
            self.assertTrue(os.path.exists(os.path.join(deliver, "Policies", "POL-GOV-001-information-security-policy.docx")))
            self.assertFalse(os.path.exists(os.path.join(deliver, "Addenda")))  # not adopted in the sample
            wb = openpyxl.load_workbook(os.path.join(deliver, "Templates", "TPL-IAM-001-quarterly-nhi-access-review.xlsx"))
            self.assertIn("Review Worksheet", wb.sheetnames)
            self.assertTrue(wb["Review Worksheet"].data_validations.dataValidation)

    def test_excel_questionnaire_round_trip(self):
        import openpyxl
        with open(SAMPLE, "rb") as fh:
            sample = tomllib.load(fh)
        with tempfile.TemporaryDirectory() as out:
            path = os.path.join(out, "q.xlsx")
            self.export.questionnaire_workbook(path, dict(self.export.DEFAULTS))
            wb = openpyxl.load_workbook(path)
            ws = wb["Questions"]
            answers = {f"scope.{k}": ("yes" if v is True else "no" if v is False else
                                      (", ".join(v) or "none") if isinstance(v, list) else v)
                       for k, v in sample["scope"].items()}
            answers["documents"] = "; ".join(f"{k}: {v}" for k, v in sample["documents"].items())
            answers.update({k: ", ".join(v) if isinstance(v, list) else v for k, v in sample["values"].items()})
            for row in ws.iter_rows(min_row=2):
                if row[0].value in answers:
                    row[6].value = answers[row[0].value]
            wb.save(path)
            config = self.intake.parse(path)
            self.assertEqual(config["scope"], sample["scope"])
            self.assertEqual(config["values"]["EFFECTIVE_DATE"], "2027-01-15")
