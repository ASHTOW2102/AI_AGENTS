import unittest
from agent import audit


class APIWebhookOutboundSSRFAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"allows_internal_ip_destinations": True, "validates_destination_url_against_allowlist": False}))

    def test_ok(self):
        self.assertFalse(audit({"allows_internal_ip_destinations": True, "validates_destination_url_against_allowlist": True}))
