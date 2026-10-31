import unittest
from agent import audit


class KubernetesSecretMountAuditTests(unittest.TestCase):
    def test_cross_namespace_access(self):
        self.assertEqual("critical", audit({"cross_namespace_secret_access": True})[-1]["severity"])

    def test_scoped_mounts(self):
        pod = {"secret_env_var_count": 0, "mounted_secrets": 1, "required_secret_count": 1,
               "secret_mount_writable": False, "cross_namespace_secret_access": False}
        self.assertEqual([], audit(pod))


if __name__ == "__main__":
    unittest.main()
