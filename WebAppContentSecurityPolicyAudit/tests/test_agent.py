import unittest
from agent import audit


class WebAppContentSecurityPolicyAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"csp_header_present": False}))

    def test_ok(self):
        self.assertFalse(audit({"csp_header_present": True, "csp_allows_unsafe_inline": False}))
