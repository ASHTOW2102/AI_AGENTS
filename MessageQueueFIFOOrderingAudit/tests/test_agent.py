import unittest
from agent import audit


class MessageQueueFIFOOrderingAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"requires_strict_ordering": True, "queue_type": "standard"}))

    def test_ok(self):
        self.assertFalse(audit({"requires_strict_ordering": True, "queue_type": "fifo"}))
