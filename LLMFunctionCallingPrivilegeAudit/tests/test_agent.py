import unittest
from agent import audit


class LLMFunctionCallingPrivilegeAuditTests(unittest.TestCase):

    def test_excess_privilege(self):
        self.assertTrue(audit({"available_tools": ["delete_account", "read_profile"], "required_tools_for_task": ["read_profile"], "high_risk_tools": ["delete_account"]}))

    def test_ok(self):
        self.assertFalse(audit({"available_tools": ["read_profile"], "required_tools_for_task": ["read_profile"], "high_risk_tools": ["delete_account"], "tool_access_scoped_per_task": True}))
