import unittest
from agent import audit


class LLMContextWindowBudgetAuditTests(unittest.TestCase):

    def test_over_budget(self):
        self.assertTrue(audit({"estimated_tokens": 9000, "model_context_limit": 8000}))

    def test_ok(self):
        self.assertFalse(audit({"estimated_tokens": 4000, "model_context_limit": 8000, "reserved_output_tokens": 1000, "min_reserved_output_tokens": 500}))
