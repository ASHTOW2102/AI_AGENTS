import unittest
from agent import audit


class APIContentNegotiationFallbackAuditTests(unittest.TestCase):

    def test_silent_fallback(self):
        self.assertTrue(audit({"unrecognized_accept_falls_back_silently": True, "fallback_documented": False}))

    def test_ok(self):
        self.assertFalse(audit({"unrecognized_accept_falls_back_silently": False, "supports_multiple_formats": True, "vary_header_includes_accept": True}))
