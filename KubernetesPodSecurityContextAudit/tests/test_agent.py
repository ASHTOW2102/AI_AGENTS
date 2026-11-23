import unittest
from agent import audit


class KubernetesPodSecurityContextAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"allow_privilege_escalation": True, "run_as_non_root": False}))

    def test_ok(self):
        self.assertFalse(audit({"allow_privilege_escalation": False, "run_as_non_root": True}))
