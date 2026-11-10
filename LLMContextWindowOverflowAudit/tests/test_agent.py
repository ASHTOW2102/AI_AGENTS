import unittest
from agent import audit


class LLMContextWindowOverflowAuditTests(unittest.TestCase):

    def test_overflow(self):
        self.assertTrue(audit({"input_tokens": 200000, "context_window_tokens": 128000}))

    def test_ok(self):
        self.assertFalse(audit({"input_tokens": 1000, "context_window_tokens": 128000, "truncation_applied": False}))
