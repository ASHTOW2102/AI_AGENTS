import unittest
from agent import audit


class SLACreditCalculationAuditTests(unittest.TestCase):

    def test_breach_no_credit(self):
        self.assertTrue(audit({"uptime_percent": 99.0, "sla_target_percent": 99.9, "credit_issued": False}))

    def test_ok(self):
        self.assertFalse(audit({"uptime_percent": 99.95, "sla_target_percent": 99.9}))
