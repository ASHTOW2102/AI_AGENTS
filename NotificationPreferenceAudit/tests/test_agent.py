import unittest
from agent import audit


class NotificationPreferenceAuditTests(unittest.TestCase):
    def test_send_after_unsubscribe(self):
        self.assertEqual("critical", audit({"unsubscribe_requested": True, "sent_after_unsubscribe": True})[0]["severity"])

    def test_valid_transactional_message(self):
        item = {"transactional": True, "contains_marketing_content": False, "preference_updated": False}
        self.assertEqual([], audit(item))


if __name__ == "__main__":
    unittest.main()
