import unittest
from agent import audit


class NetworkDNSZoneTransferAuditTests(unittest.TestCase):

    def test_open_transfer(self):
        self.assertTrue(audit({"zone_transfer_allowed_from_any": True}))

    def test_ok(self):
        self.assertFalse(audit({"zone_transfer_allowed_from_any": False, "tsig_signing_enabled": True}))
