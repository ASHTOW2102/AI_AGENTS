import unittest
from agent import audit


class WebAppOpenRedirectAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"validates_redirect_target": False}))

    def test_ok(self):
        self.assertFalse(audit({"validates_redirect_target": True, "redirect_param_allowlist": ["/home"]}))
