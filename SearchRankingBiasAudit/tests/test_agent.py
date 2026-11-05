import unittest
from agent import audit


class SearchRankingBiasAuditTests(unittest.TestCase):

    def test_source_dominance(self):
        self.assertTrue(audit({"top_result_single_source_share_percent": 80, "max_acceptable_source_share_percent": 50}))

    def test_ok(self):
        self.assertFalse(audit({"top_result_single_source_share_percent": 20, "max_acceptable_source_share_percent": 50, "sponsored_results_unlabeled": 0}))
