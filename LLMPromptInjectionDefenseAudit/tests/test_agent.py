import unittest
from agent import audit


class LLMPromptInjectionDefenseAuditTests(unittest.TestCase):

    def test_no_delimiting(self):
        self.assertTrue(audit({"processes_untrusted_input": True, "input_output_delimited": False}))

    def test_ok(self):
        self.assertFalse(audit({"processes_untrusted_input": True, "input_output_delimited": True, "model_has_tool_access": False, "system_prompt_contains_secrets": False}))
