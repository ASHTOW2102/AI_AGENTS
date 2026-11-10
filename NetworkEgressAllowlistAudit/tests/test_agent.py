import unittest
from agent import audit


class NetworkEgressAllowlistAuditTests(unittest.TestCase):

    def test_allow_all(self):
        self.assertTrue(audit({"egress_policy": "allow_all"}))

    def test_ok(self):
        self.assertFalse(audit({"egress_policy": "allowlist", "allowlist_reviewed": True}))
