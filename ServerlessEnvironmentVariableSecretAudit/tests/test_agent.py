import unittest
from agent import audit


class ServerlessEnvironmentVariableSecretAuditTests(unittest.TestCase):

    def test_plaintext_secret(self):
        self.assertTrue(audit({"env_var_names": ["DB_PASSWORD"], "secret_like_names": ["DB_PASSWORD"], "encrypted_env_vars": []}))

    def test_ok(self):
        self.assertFalse(audit({"env_var_names": ["DB_PASSWORD"], "secret_like_names": ["DB_PASSWORD"], "encrypted_env_vars": ["DB_PASSWORD"], "uses_secrets_manager": True}))
