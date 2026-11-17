import unittest
from agent import audit


class ServiceMeshFaultInjectionTestAuditTests(unittest.TestCase):

    def test_never_tested(self):
        self.assertTrue(audit({"criticality": "high", "fault_injection_tested": False}))

    def test_ok(self):
        self.assertFalse(audit({"criticality": "high", "fault_injection_tested": True, "days_since_last_test": 30, "max_acceptable_test_interval_days": 180}))
