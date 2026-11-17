import unittest
from agent import audit


class TokenBindingDeviceMismatchAuditTests(unittest.TestCase):

    def test_mismatch(self):
        self.assertTrue(audit({"token_bound_to_device": True, "current_device_fingerprint": "b", "issued_device_fingerprint": "a"}))

    def test_ok(self):
        self.assertFalse(audit({"token_bound_to_device": True, "current_device_fingerprint": "a", "issued_device_fingerprint": "a"}))
