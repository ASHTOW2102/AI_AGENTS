import unittest
from agent import audit


class LLMToolCallValidationAuditTests(unittest.TestCase):

    def test_unvalidated(self):
        self.assertTrue(audit({"executes_tool_calls": True, "argument_schema_validated": False}))

    def test_ok(self):
        self.assertFalse(audit({"executes_tool_calls": True, "argument_schema_validated": True, "destructive_tools_require_confirmation": True}))
