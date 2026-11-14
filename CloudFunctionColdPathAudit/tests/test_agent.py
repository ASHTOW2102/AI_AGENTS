import unittest
from agent import audit


class CloudFunctionColdPathAuditTests(unittest.TestCase):

    def test_untested_cold_path(self):
        self.assertTrue(audit({"error_path_invocation_count": 0, "has_error_handling_code": True, "error_path_unit_tested": False}))

    def test_ok(self):
        self.assertFalse(audit({"error_path_invocation_count": 10, "has_error_handling_code": True, "error_path_unit_tested": True}))
