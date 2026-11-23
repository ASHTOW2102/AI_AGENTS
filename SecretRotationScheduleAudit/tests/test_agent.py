import unittest
from agent import audit


class SecretRotationScheduleAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"last_rotated_days_ago": 120, "max_rotation_interval_days": 90}))

    def test_ok(self):
        self.assertFalse(audit({"last_rotated_days_ago": 30, "max_rotation_interval_days": 90}))
