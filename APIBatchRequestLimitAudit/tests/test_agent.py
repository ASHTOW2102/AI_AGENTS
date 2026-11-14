import unittest
from agent import audit


class APIBatchRequestLimitAuditTests(unittest.TestCase):

    def test_no_limit(self):
        self.assertTrue(audit({"max_batch_size": None}))

    def test_ok(self):
        self.assertFalse(audit({"max_batch_size": 50, "recommended_max_batch_size": 100}))
