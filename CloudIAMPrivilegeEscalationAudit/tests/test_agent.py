import unittest
from agent import audit


class CloudIAMPrivilegeEscalationAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"has_pass_role_permission": True, "has_create_policy_permission": True}))

    def test_ok(self):
        self.assertFalse(audit({"has_pass_role_permission": True, "has_create_policy_permission": False}))
