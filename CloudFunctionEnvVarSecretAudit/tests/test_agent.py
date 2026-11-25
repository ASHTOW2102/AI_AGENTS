import unittest
from agent import audit


class CloudFunctionEnvVarSecretAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"env_vars": {"DB_PASSWORD": "x", "REGION": "us-east-1"}, "uses_secret_manager": False}))

    def test_ok(self):
        self.assertFalse(audit({"env_vars": {"DB_PASSWORD": "x"}, "uses_secret_manager": True}))
