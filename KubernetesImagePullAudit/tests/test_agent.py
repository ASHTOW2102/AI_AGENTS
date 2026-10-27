import unittest
from agent import audit


class KubernetesImagePullAuditTests(unittest.TestCase):
    def test_latest_tag(self):
        self.assertIn("explicit version", audit({"images": [{"reference": "demo:latest"}]})[0]["issue"])

    def test_reproducible_pull(self):
        workload = {"images": [{"reference": "repo/app:2.1", "digest_pinned": True}],
                    "pull_policy": "IfNotPresent"}
        self.assertEqual([], audit(workload))


if __name__ == "__main__":
    unittest.main()
