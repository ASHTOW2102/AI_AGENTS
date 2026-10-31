import unittest
from agent import audit


class QueueOrderingGuaranteeAuditTests(unittest.TestCase):
    def test_missing_partition_key(self):
        self.assertIn("no partition key", audit({"ordering_required": True})[0]["issue"])

    def test_ordered_queue(self):
        queue = {"ordering_required": True, "partition_key": "account_id", "consumer_parallelism": 4,
                 "per_key_serialization": True, "retry_can_reorder": False}
        self.assertEqual([], audit(queue))


if __name__ == "__main__":
    unittest.main()
