import unittest
from agent import audit


class WebAppReferrerPolicyAuditTests(unittest.TestCase):

    def test_missing(self):
        self.assertTrue(audit({"referrer_policy": None}))

    def test_ok(self):
        self.assertFalse(audit({"referrer_policy": "strict-origin-when-cross-origin", "urls_contain_sensitive_query_params": False}))
