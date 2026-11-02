import unittest
from agent import audit


class ContainerNonRootUserAuditTests(unittest.TestCase):

    def test_root_user(self):
        self.assertTrue(audit({"run_as_user": 0, "allow_privilege_escalation": False}))

    def test_ok(self):
        self.assertFalse(audit({"run_as_user": 1000, "allow_privilege_escalation": False, "read_only_root_filesystem": True}))
