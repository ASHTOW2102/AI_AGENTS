import unittest
from agent import audit


class ContainerRuntimeSeccompAuditTests(unittest.TestCase):
    def test_unconfined_profile(self):
        self.assertIn("seccomp", audit({"seccomp_profile": "unconfined"})[0]["issue"])

    def test_restricted_runtime(self):
        runtime = {"seccomp_profile": "runtime/default", "privilege_escalation_allowed": False,
                   "root_user": False, "unmasked_proc": False}
        self.assertEqual([], audit(runtime))


if __name__ == "__main__":
    unittest.main()
