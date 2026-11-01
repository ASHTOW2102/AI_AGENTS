import unittest
from agent import audit


class SOC2EvidenceAuditTests(unittest.TestCase):

    def test_no_owner(self):
        self.assertTrue(audit({"owner": None}))

    def test_ok(self):
        self.assertFalse(audit({"owner": "team", "evidence_age_days": 10, "tested_this_period": True}))
