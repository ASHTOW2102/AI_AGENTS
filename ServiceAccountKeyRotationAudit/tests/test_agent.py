import unittest
from agent import audit


class ServiceAccountKeyRotationAuditTests(unittest.TestCase):

    def test_no_rotation_policy(self):
        self.assertTrue(audit({"has_rotation_policy": False, "key_age_days": 10}))

    def test_ok(self):
        self.assertFalse(audit({"has_rotation_policy": True, "key_age_days": 30, "max_allowed_age_days": 90}))
