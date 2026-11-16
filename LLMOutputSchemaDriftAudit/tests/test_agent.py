import unittest
from agent import audit


class LLMOutputSchemaDriftAuditTests(unittest.TestCase):

    def test_unalerted_failures(self):
        self.assertTrue(audit({"schema_validation_failures_last_24h": 5, "validation_failures_alerted": False}))

    def test_ok(self):
        self.assertFalse(audit({"schema_validation_failures_last_24h": 0, "validation_failures_alerted": True, "output_schema_validated": True}))
