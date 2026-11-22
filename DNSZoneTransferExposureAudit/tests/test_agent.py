import unittest
from agent import audit


class DNSZoneTransferExposureAuditTests(unittest.TestCase):

    def test_open_axfr(self):
        self.assertTrue(audit({"axfr_restricted_to_secondaries": False}))

    def test_ok(self):
        self.assertFalse(audit({"axfr_restricted_to_secondaries": True, "exposes_internal_subdomains_in_zone": False}))
