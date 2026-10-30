import unittest
from agent import audit


class LLMToolPermissionAuditTests(unittest.TestCase):
    def test_side_effect_without_approval(self):
        self.assertEqual("critical", audit({"side_effecting": True, "human_approval_required": False})[0]["severity"])

    def test_least_privilege_tool(self):
        tool = {"granted_actions": ["read"], "required_actions": ["read"],
                "side_effecting": False, "audit_log_enabled": True}
        self.assertEqual([], audit(tool))


if __name__ == "__main__":
    unittest.main()
