import unittest
from agent import audit


class LLMOutputSchemaAuditTests(unittest.TestCase):
    def test_missing_validation(self):
        self.assertIn("not validated", audit({})[0]["issue"])

    def test_validated_contract(self):
        contract = {"schema_validation": True, "invalid_output_handling": True,
                    "strict_json_expected": True, "freeform_fallback": False,
                    "sensitive_fields": False}
        self.assertEqual([], audit(contract))


if __name__ == "__main__":
    unittest.main()
