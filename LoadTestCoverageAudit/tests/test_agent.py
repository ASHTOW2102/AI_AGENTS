import unittest
from agent import audit


class LoadTestCoverageAuditTests(unittest.TestCase):

    def test_stale_test(self):
        self.assertTrue(audit({"days_since_last_load_test": 300, "max_days_between_tests": 180}))

    def test_ok(self):
        self.assertFalse(audit({"days_since_last_load_test": 30, "last_test_peak_rps": 1000, "projected_peak_rps": 800}))
