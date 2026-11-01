import unittest
from agent import audit


class WebhookEndpointTLSAuditTests(unittest.TestCase):

    def test_http_allowed(self):
        self.assertTrue(audit({"https_only": False}))

    def test_ok(self):
        self.assertFalse(audit({"https_only": True, "certificate_validation_disabled": False}))
