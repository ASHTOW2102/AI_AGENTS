import unittest
from agent import audit


class QueueConsumerConcurrencyAuditTests(unittest.TestCase):
    def test_unbounded_downstream_load(self):
        self.assertIn("downstream capacity", audit({"concurrency_enabled": True,
                                                     "downstream_capacity_budgeted": False})[0]["issue"])

    def test_ordered_processing(self):
        consumer = {"concurrency_enabled": True, "downstream_capacity_budgeted": True,
                    "ordering_required": True, "parallelism": 4, "key_ordering_preserved": True,
                    "max_inflight_messages": 10, "approved_max_inflight": 20}
        self.assertEqual([], audit(consumer))


if __name__ == "__main__":
    unittest.main()
