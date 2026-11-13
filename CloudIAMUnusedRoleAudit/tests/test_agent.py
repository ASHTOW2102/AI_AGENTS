import unittest
from agent import audit


class CloudIAMUnusedRoleAuditTests(unittest.TestCase):

    def test_stale(self):
        self.assertTrue(audit({"days_since_last_use": 200, "max_acceptable_unused_days": 90}))

    def test_ok(self):
        self.assertFalse(audit({"days_since_last_use": 5, "max_acceptable_unused_days": 90, "grants_admin_access": False}))
