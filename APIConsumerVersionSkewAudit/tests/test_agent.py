import unittest
from agent import audit


class APIConsumerVersionSkewAuditTests(unittest.TestCase):

    def test_overdue(self):
        self.assertTrue(audit({"client_version_deprecated": True, "days_since_deprecation": 200, "max_grace_period_days": 180}))

    def test_ok(self):
        self.assertFalse(audit({"client_version_deprecated": True, "days_since_deprecation": 10, "max_grace_period_days": 180, "upgrade_notified": True}))
