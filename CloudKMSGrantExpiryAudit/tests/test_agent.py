import unittest
from agent import audit


class CloudKMSGrantExpiryAuditTests(unittest.TestCase):

    def test_no_expiry(self):
        self.assertTrue(audit({"expiry_set": False}))

    def test_ok(self):
        self.assertFalse(audit({"expiry_set": True, "expiry_days": 30, "max_acceptable_expiry_days": 90}))
