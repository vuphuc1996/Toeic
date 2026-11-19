from __future__ import annotations

import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "audit-design-tokens.py"
REPO = SCRIPT.parents[1]
SPEC = importlib.util.spec_from_file_location("audit_design_tokens", SCRIPT)
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class DesignTokenAuditTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "tools").mkdir()
        (self.root / "assets/css").mkdir(parents=True)
        (self.root / "design").mkdir()
        shutil.copy2(REPO / "tools/design-token-rules.json", self.root / "tools/design-token-rules.json")
        (self.root / "design/design-profile.json").write_text(json.dumps({
            "cssVariables": {"--ds-color-brand": "#1D568F", "--ds-color-surface": "#FFFFFF"}
        }), encoding="utf-8")
        (self.root / "assets/css/design-system.css").write_text(
            ":root { --ds-color-brand: #1D568F; --ds-font-body: 15px; }\n", encoding="utf-8"
        )
        (self.root / "assets/css/app.css").write_text("", encoding="utf-8")
        self.rules_path = self.root / "tools/design-token-rules.json"
        self.baseline_path = self.root / "tools/design-token-baseline.json"

    def tearDown(self):
        self.tmp.cleanup()

    def write_css(self, css):
        (self.root / "assets/css/app.css").write_text(css, encoding="utf-8")

    def bootstrap_baseline(self):
        AUDIT.bootstrap_baseline(self.root, self.baseline_path, self.rules_path)

    def test_valid_tokens_pass_all_design_rules(self):
        self.write_css("""
        .panel {
          font-size: var(--ds-font-body);
          font-weight: 700;
          border-radius: var(--ds-radius-card);
          box-shadow: var(--ds-shadow-card);
          color: var(--ds-color-brand);
        }
        @media (max-width: 640px) { .panel { padding: 8px; } }
        """)
        self.bootstrap_baseline()
        result = AUDIT.audit_project(self.root, self.baseline_path, self.rules_path)
        self.assertTrue(result["ok"])
        self.assertEqual(result["new"], [])
        self.assertEqual(result["legacy"], [])

    def test_each_rule_rejects_an_out_of_contract_value(self):
        self.write_css("""
        .bad {
          font-size: 11px;
          font-weight: 650;
          border-radius: 7px;
          box-shadow: 0 3px 9px #123456;
          color: #ABCDEF !important;
        }
        @media (max-width: 777px) { .bad { padding: 4px; } }
        """)
        findings, _ = AUDIT.collect_audit(self.root, AUDIT.load_json(self.rules_path))
        rules = {item["rule"] for item in findings}
        self.assertTrue({"FONT-SIZE", "FONT-WEIGHT", "BORDER-RADIUS", "BOX-SHADOW", "HEX-COLOR", "IMPORTANT", "BREAKPOINT"}.issubset(rules))

    def test_existing_legacy_violation_is_warning_not_error(self):
        self.write_css(".legacy { font-size: 11px; }")
        self.bootstrap_baseline()
        result = AUDIT.audit_project(self.root, self.baseline_path, self.rules_path)
        self.assertTrue(result["ok"])
        self.assertEqual(len(result["legacy"]), 1)
        self.assertEqual(result["new"], [])

    def test_new_violation_fails_ci(self):
        self.write_css(".legacy { font-size: 11px; }")
        self.bootstrap_baseline()
        self.write_css(".legacy { font-size: 11px; }\n.new-feature { font-size: 10px; }")
        result = AUDIT.audit_project(self.root, self.baseline_path, self.rules_path)
        self.assertFalse(result["ok"])
        self.assertEqual(len(result["new"]), 1)
        self.assertEqual(result["new"][0]["selector"], ".new-feature")

    def test_new_value_on_existing_selector_property_is_rejected(self):
        self.write_css(".legacy { font-size: 11px; }")
        self.bootstrap_baseline()
        self.write_css(".legacy { font-size: 10px; }")
        result = AUDIT.audit_project(self.root, self.baseline_path, self.rules_path)
        self.assertFalse(result["ok"])
        self.assertEqual(len(result["new"]), 1)

    def test_removed_legacy_violation_is_detected_as_resolved(self):
        self.write_css(".legacy { font-size: 11px; }")
        self.bootstrap_baseline()
        self.write_css(".legacy { font-size: var(--ds-font-body); }")
        result = AUDIT.audit_project(self.root, self.baseline_path, self.rules_path)
        self.assertTrue(result["ok"])
        self.assertEqual(len(result["resolved"]), 1)

    def test_rule_parameter_change_raises_rule_drift(self):
        self.write_css(".legacy { font-size: 11px; }")
        self.bootstrap_baseline()
        rules = AUDIT.load_json(self.rules_path)
        rules["fontWeight"]["allowed"].append(900)  # simulated rule loosening
        self.rules_path.write_text(json.dumps(rules, indent=2) + "\n", encoding="utf-8")
        result = AUDIT.audit_project(self.root, self.baseline_path, self.rules_path)
        self.assertTrue(result["ruleDrift"])
        self.assertFalse(result["ok"])

    def test_baseline_is_never_overwritten(self):
        self.write_css(".legacy { font-size: 11px; }")
        self.bootstrap_baseline()
        before = self.baseline_path.read_bytes()
        with self.assertRaises(FileExistsError):
            self.bootstrap_baseline()
        self.assertEqual(self.baseline_path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
