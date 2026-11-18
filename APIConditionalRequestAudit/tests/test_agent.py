import unittest
from agent import audit


class APIConditionalRequestAuditTests(unittest.TestCase):

    def test_no_conditional(self):
        self.assertTrue(audit({"supports_concurrent_writes": True, "supports_etag_conditional_requests": False}))

    def test_ok(self):
        self.assertFalse(audit({"supports_concurrent_writes": True, "supports_etag_conditional_requests": True, "returns_412_on_mismatch": True}))
