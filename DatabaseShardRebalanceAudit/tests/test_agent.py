import unittest
from agent import audit


class DatabaseShardRebalanceAuditTests(unittest.TestCase):

    def test_hot_shard(self):
        self.assertTrue(audit({"max_shard_size_ratio": 2.0, "max_allowed_size_ratio": 1.5}))

    def test_ok(self):
        self.assertFalse(audit({"max_shard_size_ratio": 1.1, "max_allowed_size_ratio": 1.5, "hot_shard_qps_ratio": 1.0}))
