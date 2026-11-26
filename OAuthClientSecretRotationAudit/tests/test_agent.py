import unittest
from agent import audit


class OAuthClientSecretRotationAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"secret_last_rotated_days_ago": 200, "max_rotation_interval_days": 90}))

    def test_ok(self):
        self.assertFalse(audit({"secret_last_rotated_days_ago": 30, "max_rotation_interval_days": 90}))
