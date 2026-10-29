import unittest
from agent import audit


class APIResponseCompressionAuditTests(unittest.TestCase):
    def test_secret_reflection_compression(self):
        self.assertIn("attacker-controlled", audit({"compress_secrets_with_reflected_input": True})[0]["issue"])

    def test_bounded_compression(self):
        endpoint = {"compression_enabled": True, "minimum_size_threshold_bytes": 1024,
                    "content_type_allowlist": ["application/json"],
                    "compress_secrets_with_reflected_input": False,
                    "max_uncompressed_response_bytes": 10000, "approved_max_response_bytes": 20000}
        self.assertEqual([], audit(endpoint))


if __name__ == "__main__":
    unittest.main()
