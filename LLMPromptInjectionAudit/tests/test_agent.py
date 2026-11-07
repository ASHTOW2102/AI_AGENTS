import unittest
from agent import audit


class LLMPromptInjectionAuditTests(unittest.TestCase):

    def test_unisolated(self):
        self.assertTrue(audit({"untrusted_content_in_prompt": True, "content_delimiting_enforced": False}))

    def test_ok(self):
        self.assertFalse(audit({"untrusted_content_in_prompt": True, "content_delimiting_enforced": True, "output_action_allowlist": True}))
