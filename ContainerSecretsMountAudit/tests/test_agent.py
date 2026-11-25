import unittest
from agent import audit


class ContainerSecretsMountAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"mounts_secrets_as_env_vars": True}))

    def test_ok(self):
        self.assertFalse(audit({"mounts_secrets_as_env_vars": False, "mounts_secrets_as_files": True}))
