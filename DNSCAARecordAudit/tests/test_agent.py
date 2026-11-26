import unittest
from agent import audit


class DNSCAARecordAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"issues_certificates": True, "has_caa_record": False}))

    def test_ok(self):
        self.assertFalse(audit({"issues_certificates": True, "has_caa_record": True}))
