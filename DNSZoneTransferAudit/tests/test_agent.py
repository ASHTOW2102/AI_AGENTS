import unittest
from agent import audit


class DNSZoneTransferAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"allows_axfr_from_any": True}))

    def test_ok(self):
        self.assertFalse(audit({"allows_axfr_from_any": False, "zone_transfer_restricted_to": ["10.0.0.5"]}))
