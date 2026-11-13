import unittest
from agent import audit


class TokenReplayWindowAuditTests(unittest.TestCase):

    def test_no_nonce_tracking(self):
        self.assertTrue(audit({"nonce_tracking_enabled": False, "single_use_intended": True}))

    def test_ok(self):
        self.assertFalse(audit({"nonce_tracking_enabled": True, "single_use_intended": True, "replay_window_seconds": 5, "validity_seconds": 300}))
