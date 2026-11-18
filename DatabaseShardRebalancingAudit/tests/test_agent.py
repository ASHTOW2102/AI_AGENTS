import unittest
from agent import audit


class DatabaseShardRebalancingAuditTests(unittest.TestCase):

    def test_skewed(self):
        self.assertTrue(audit({"shard_sizes_gb": [10, 100], "max_acceptable_skew_ratio": 2.0}))

    def test_ok(self):
        self.assertFalse(audit({"shard_sizes_gb": [50, 55], "max_acceptable_skew_ratio": 2.0, "automated_rebalancing_enabled": True}))
