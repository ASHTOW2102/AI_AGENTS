import unittest
from agent import audit


class APIBackwardCompatibilityTestAuditTests(unittest.TestCase):

    def test_no_compat_test(self):
        self.assertTrue(audit({"public_api_changed": True, "backward_compat_test_run": False}))

    def test_ok(self):
        self.assertFalse(audit({"public_api_changed": True, "backward_compat_test_run": True, "breaking_changes_detected": 0, "contract_test_baseline_pinned": True}))
