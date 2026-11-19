import unittest
from agent import audit


class WebAppMixedContentAuditTests(unittest.TestCase):

    def test_mixed_content(self):
        self.assertTrue(audit({"served_over_https": True, "http_active_content_urls": ["http://cdn.example.com/x.js"]}))

    def test_ok(self):
        self.assertFalse(audit({"served_over_https": True, "http_active_content_urls": [], "upgrade_insecure_requests_enabled": True}))
