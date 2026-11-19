import unittest
from agent import audit


class LLMRetrievalChunkLeakageAuditTests(unittest.TestCase):

    def test_no_filter(self):
        self.assertTrue(audit({"retrieval_spans_multiple_permission_levels": True, "retrieval_filters_by_requester_permissions": False}))

    def test_ok(self):
        self.assertFalse(audit({"retrieval_spans_multiple_permission_levels": True, "retrieval_filters_by_requester_permissions": True, "filter_tested_for_bypass": True}))
