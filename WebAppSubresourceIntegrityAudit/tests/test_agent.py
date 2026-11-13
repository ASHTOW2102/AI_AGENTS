import unittest
from agent import audit


class WebAppSubresourceIntegrityAuditTests(unittest.TestCase):

    def test_unprotected(self):
        self.assertTrue(audit({"third_party_scripts": ["cdn.js"], "sri_protected_scripts": []}))

    def test_ok(self):
        self.assertFalse(audit({"third_party_scripts": ["cdn.js"], "sri_protected_scripts": ["cdn.js"], "crossorigin_attribute_set": True}))
