import unittest
from agent import audit


class WebAppCDNScriptIntegrityAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"loads_third_party_scripts": True, "uses_subresource_integrity": False}))

    def test_ok(self):
        self.assertFalse(audit({"loads_third_party_scripts": True, "uses_subresource_integrity": True}))
