import unittest
from agent import audit


class KubernetesResourceRequestAuditTests(unittest.TestCase):
    def test_missing_resources(self):
        self.assertEqual(4, len(audit({"containers": [{"name": "api"}]})))

    def test_valid_resources(self):
        item = {"containers": [{"name": "api", "requests": {"cpu": 1, "memory": 256},
                                "limits": {"cpu": 2, "memory": 512}}]}
        self.assertEqual([], audit(item))


if __name__ == "__main__":
    unittest.main()
