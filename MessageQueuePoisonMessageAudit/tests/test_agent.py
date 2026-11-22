import unittest
from agent import audit


class MessageQueuePoisonMessageAuditTests(unittest.TestCase):

    def test_no_dlq_no_max_retries(self):
        self.assertTrue(audit({"has_dead_letter_queue": False, "max_delivery_attempts": None}))

    def test_ok(self):
        self.assertFalse(audit({"has_dead_letter_queue": True, "max_delivery_attempts": 5}))
