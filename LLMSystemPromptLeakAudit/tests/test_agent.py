import unittest
from agent import audit


class LLMSystemPromptLeakAuditTests(unittest.TestCase):

    def test_secrets_in_prompt(self):
        self.assertTrue(audit({"system_prompt_contains_secrets": True}))

    def test_ok(self):
        self.assertFalse(audit({"system_prompt_contains_secrets": False, "prompt_leak_mitigation_tested": True}))
