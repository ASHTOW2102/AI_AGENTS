import unittest
from agent import audit


class WebhookDeadLetterAuditTests(unittest.TestCase):

    def test_no_dead_letter(self):
        self.assertTrue(audit({"max_retries_exhausted_count": 3, "dead_letter_storage_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"max_retries_exhausted_count": 0, "dead_letter_storage_configured": True, "dead_letter_alerting": True}))
