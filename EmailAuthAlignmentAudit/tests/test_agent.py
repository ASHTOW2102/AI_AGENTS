import unittest
from agent import audit


class EmailAuthAlignmentAuditTests(unittest.TestCase):

    def test_missing_spf(self):
        self.assertTrue(audit({"spf_present": False}))

    def test_ok(self):
        self.assertFalse(audit({"spf_present": True, "dkim_present": True, "dmarc_policy": "quarantine"}))
