import unittest
from agent import audit


class ChaosEngineeringReadinessAuditTests(unittest.TestCase):

    def test_missing_limit(self):
        self.assertTrue(audit({"blast_radius_limited": False}))

    def test_ok(self):
        self.assertFalse(audit({"blast_radius_limited": True, "automatic_abort_configured": True, "rollback_plan": "x"}))
