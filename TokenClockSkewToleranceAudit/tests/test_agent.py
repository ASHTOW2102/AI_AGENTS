import unittest
from agent import audit


class TokenClockSkewToleranceAuditTests(unittest.TestCase):

    def test_loose_tolerance(self):
        self.assertTrue(audit({"clock_skew_tolerance_seconds": 600, "max_acceptable_tolerance_seconds": 60}))

    def test_ok(self):
        self.assertFalse(audit({"clock_skew_tolerance_seconds": 30, "max_acceptable_tolerance_seconds": 60, "clock_skew_tolerance_configured": True}))
