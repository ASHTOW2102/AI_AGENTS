import unittest
from agent import audit


class MobileAppLinkVerificationAuditTests(unittest.TestCase):

    def test_not_published(self):
        self.assertTrue(audit({"assetlinks_or_aasa_published": False}))

    def test_ok(self):
        self.assertFalse(audit({"assetlinks_or_aasa_published": True, "package_fingerprint_matches": True}))
