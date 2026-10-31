import unittest
from agent import audit


class DataLakePartitionPruningAuditTests(unittest.TestCase):
    def test_missing_partition_filter(self):
        self.assertIn("partition key", audit({"partitioned_table": True})[0]["issue"])

    def test_bounded_scan(self):
        query = {"partitioned_table": True, "partition_filter_present": True,
                 "estimated_scanned_bytes": 100, "max_scanned_bytes": 1000,
                 "partition_count_scanned": 2, "max_partitions_scanned": 10}
        self.assertEqual([], audit(query))


if __name__ == "__main__":
    unittest.main()
