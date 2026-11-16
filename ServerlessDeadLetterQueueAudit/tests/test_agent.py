import unittest
from agent import audit


class ServerlessDeadLetterQueueAuditTests(unittest.TestCase):

    def test_no_dlq(self):
        self.assertTrue(audit({"invocation_type": "async", "dead_letter_queue_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"invocation_type": "async", "dead_letter_queue_configured": True, "dlq_alerting_enabled": True}))
