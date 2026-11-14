import unittest
from agent import audit


class ServerlessIAMOverPermissionAuditTests(unittest.TestCase):

    def test_wildcard(self):
        self.assertTrue(audit({"granted_actions": ["*"], "used_actions": ["s3:GetObject"]}))

    def test_ok(self):
        self.assertFalse(audit({"granted_actions": ["s3:GetObject"], "used_actions": ["s3:GetObject"]}))
