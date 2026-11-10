import unittest
from agent import audit


class FeatureFlagStaleCleanupAuditTests(unittest.TestCase):

    def test_overdue(self):
        self.assertTrue(audit({"rollout_percent": 100, "days_since_full_rollout": 120, "max_cleanup_days": 60}))

    def test_ok(self):
        self.assertFalse(audit({"rollout_percent": 100, "days_since_full_rollout": 10, "max_cleanup_days": 60, "cleanup_ticket_filed": True}))
