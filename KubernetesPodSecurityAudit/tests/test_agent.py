import unittest
from agent import audit


class KubernetesPodSecurityAuditTests(unittest.TestCase):
    def test_privileged_pod(self):
        self.assertEqual("critical", audit({"privileged": True})[0]["severity"])

    def test_restricted_pod(self):
        pod = {"privileged": False, "run_as_root": False, "host_network": False, "host_pid": False,
               "read_only_root_filesystem": True, "capabilities_added": []}
        self.assertEqual([], audit(pod))


if __name__ == "__main__":
    unittest.main()
