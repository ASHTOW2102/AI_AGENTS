import unittest
from agent import audit


class DockerBuildContextAuditTests(unittest.TestCase):
    def test_secret_in_context(self):
        self.assertEqual("critical", audit({"secrets_in_context": 1})[0]["severity"])

    def test_clean_context(self):
        build = {"secrets_in_context": 0, "excluded_patterns_missing": False,
                 "context_size_bytes": 1000, "max_context_size_bytes": 10000,
                 "dockerfile_outside_context": False}
        self.assertEqual([], audit(build))


if __name__ == "__main__":
    unittest.main()
