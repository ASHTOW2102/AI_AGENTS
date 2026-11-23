import unittest
from agent import audit


class OAuthRedirectURIValidationAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"redirect_uri_validation": "wildcard"}))

    def test_ok(self):
        self.assertFalse(audit({"redirect_uri_validation": "exact"}))
