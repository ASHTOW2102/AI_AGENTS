import unittest
from agent import audit


class SearchQueryLoggingPrivacyAuditTests(unittest.TestCase):

    def test_unredacted(self):
        self.assertTrue(audit({"logs_raw_query_text": True, "pii_redaction_applied": False}))

    def test_ok(self):
        self.assertFalse(audit({"logs_raw_query_text": True, "pii_redaction_applied": True, "query_linked_to_user_id": False}))
