import unittest
from agent import audit


class APIRequestCollapsingAuditTests(unittest.TestCase):

    def test_no_collapsing(self):
        self.assertTrue(audit({"is_expensive_operation": True, "request_collapsing_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"is_expensive_operation": True, "request_collapsing_enabled": True, "collapsing_key_includes_auth_scope": True}))
