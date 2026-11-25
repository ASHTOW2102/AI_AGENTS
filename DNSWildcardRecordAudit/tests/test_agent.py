import unittest
from agent import audit


class DNSWildcardRecordAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"has_wildcard_record": True, "wildcard_target_verified": False}))

    def test_ok(self):
        self.assertFalse(audit({"has_wildcard_record": True, "wildcard_target_verified": True}))
