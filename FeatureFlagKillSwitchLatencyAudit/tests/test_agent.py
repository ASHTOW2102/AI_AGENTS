import unittest
from agent import audit


class FeatureFlagKillSwitchLatencyAuditTests(unittest.TestCase):

    def test_slow_propagation(self):
        self.assertTrue(audit({"is_kill_switch": True, "propagation_latency_seconds": 120, "max_acceptable_latency_seconds": 30}))

    def test_ok(self):
        self.assertFalse(audit({"is_kill_switch": True, "propagation_latency_seconds": 5, "max_acceptable_latency_seconds": 30, "last_tested_date": "2026-01-01", "requires_deploy_to_toggle": False}))
