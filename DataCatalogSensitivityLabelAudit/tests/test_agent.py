import unittest
from agent import audit


class DataCatalogSensitivityLabelAuditTests(unittest.TestCase):

    def test_unlabeled(self):
        self.assertTrue(audit({"contains_sensitive_pattern": True, "sensitivity_label_applied": False}))

    def test_ok(self):
        self.assertFalse(audit({"contains_sensitive_pattern": True, "sensitivity_label_applied": True, "label_last_reviewed_days_ago": 10, "max_acceptable_review_interval_days": 365}))
