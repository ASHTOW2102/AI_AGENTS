import unittest
from agent import audit


class DataPartitionSkewAuditTests(unittest.TestCase):
    def test_skewed_partition_sizes(self):
        self.assertIn("skew ratio", audit({"partition_sizes": [1, 10], "max_size_ratio": 3})[0]["issue"])

    def test_balanced_distribution(self):
        profile = {"partition_sizes": [5, 6, 7], "partition_loads": [10, 11, 9],
                   "max_size_ratio": 3, "max_load_ratio": 3, "empty_partitions": 0}
        self.assertEqual([], audit(profile))


if __name__ == "__main__":
    unittest.main()
