import unittest
from agent import audit


class KafkaPartitionBalanceAuditTests(unittest.TestCase):
    def test_offline_partition_is_critical(self):
        self.assertEqual("critical", audit({"offline_partitions": 1})[0]["severity"])

    def test_balanced_cluster(self):
        cluster = {"partitions_per_broker": [20, 21], "leaders_per_broker": [10, 11],
                   "under_replicated_partitions": 0, "offline_partitions": 0}
        self.assertEqual([], audit(cluster))


if __name__ == "__main__":
    unittest.main()
