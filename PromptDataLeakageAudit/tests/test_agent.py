import unittest
from agent import audit


class PromptDataLeakageAuditTests(unittest.TestCase):
    def test_secret_in_prompt(self):
        self.assertEqual("critical", audit({"secrets_in_prompt": True})[0]["severity"])

    def test_redacted_prompt_flow(self):
        flow = {"personal_data_in_prompt": False, "secrets_in_prompt": False,
                "external_model": True, "provider_retention_reviewed": True,
                "prompt_logging_enabled": True, "sensitive_log_redaction": True}
        self.assertEqual([], audit(flow))


if __name__ == "__main__":
    unittest.main()
