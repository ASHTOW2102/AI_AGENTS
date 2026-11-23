import unittest
from agent import audit


class MessageQueueDeadLetterAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"dead_letter_queue_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"dead_letter_queue_configured": True, "max_receive_count": 5}))
