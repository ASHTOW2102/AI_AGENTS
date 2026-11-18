import unittest
from agent import audit


class LLMEmbeddingPoisoningAuditTests(unittest.TestCase):

    def test_unmoderated(self):
        self.assertTrue(audit({"indexes_user_submitted_content": True, "content_moderation_before_indexing": False}))

    def test_ok(self):
        self.assertFalse(audit({"indexes_user_submitted_content": True, "content_moderation_before_indexing": True, "retrieval_source_segregated_by_trust_level": True}))
