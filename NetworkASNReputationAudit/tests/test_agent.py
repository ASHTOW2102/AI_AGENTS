import unittest
from agent import audit


class NetworkASNReputationAuditTests(unittest.TestCase):

    def test_unblocked_bad_asn(self):
        self.assertTrue(audit({"source_asn_reputation_score": 10, "min_acceptable_reputation_score": 40, "blocked": False}))

    def test_ok(self):
        self.assertFalse(audit({"source_asn_reputation_score": 90, "min_acceptable_reputation_score": 40, "blocked": False, "asn_reputation_checked": True}))
