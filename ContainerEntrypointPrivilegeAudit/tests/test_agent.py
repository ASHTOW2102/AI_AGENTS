import unittest
from agent import audit


class ContainerEntrypointPrivilegeAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"runs_as_root": True, "entrypoint_user": "root"}))

    def test_ok(self):
        self.assertFalse(audit({"runs_as_root": False, "entrypoint_user": "appuser"}))
