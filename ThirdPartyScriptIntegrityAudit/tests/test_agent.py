import unittest
from agent import audit


class ThirdPartyScriptIntegrityAuditTests(unittest.TestCase):

    def test_no_integrity(self):
        self.assertTrue(audit({"third_party": True, "integrity_hash": None}))

    def test_ok(self):
        self.assertFalse(audit({"third_party": True, "integrity_hash": "sha384-x", "crossorigin": "anonymous"}))
