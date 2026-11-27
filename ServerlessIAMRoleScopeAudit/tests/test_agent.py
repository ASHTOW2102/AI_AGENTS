import unittest
from agent import audit


class ServerlessIAMRoleScopeAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"iam_role_allows_wildcard_resource": True}))

    def test_ok(self):
        self.assertFalse(audit({"iam_role_allows_wildcard_resource": False}))
