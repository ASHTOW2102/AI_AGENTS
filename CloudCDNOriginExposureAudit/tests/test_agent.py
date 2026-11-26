import unittest
from agent import audit


class CloudCDNOriginExposureAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"origin_publicly_accessible": True, "origin_restricted_to_cdn_ips": False}))

    def test_ok(self):
        self.assertFalse(audit({"origin_publicly_accessible": True, "origin_restricted_to_cdn_ips": True}))
