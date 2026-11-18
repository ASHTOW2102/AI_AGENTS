import unittest
from agent import audit


class APIGraphQLBatchingAbuseAuditTests(unittest.TestCase):

    def test_unbounded_batch(self):
        self.assertTrue(audit({"max_batch_size": None}))

    def test_ok(self):
        self.assertFalse(audit({"max_batch_size": 1, "rate_limit_applies_per": "query"}))
