import unittest
from agent import audit


class DatabasePartitionPruningAuditTests(unittest.TestCase):

    def test_no_pruning(self):
        self.assertTrue(audit({"partitioned_table": True, "partition_key_in_predicate": False}))

    def test_ok(self):
        self.assertFalse(audit({"partitioned_table": True, "partition_key_in_predicate": True, "partitions_scanned": 1, "partitions_expected": 1}))
