import unittest
from agent import audit


class MobilePushTokenAuditTests(unittest.TestCase):

    def test_stale(self):
        self.assertTrue(audit({"age_days": 400, "max_valid_age_days": 270}))

    def test_ok(self):
        self.assertFalse(audit({"age_days": 10, "delivery_failures_in_a_row": 0, "user_logged_out": False}))
