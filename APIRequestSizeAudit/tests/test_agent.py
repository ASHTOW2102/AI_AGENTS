import unittest
from agent import audit


class APIRequestSizeAuditTests(unittest.TestCase):
    def test_unbounded_stream(self):
        self.assertTrue(any("total size" in f["issue"] for f in audit({"max_body_bytes": 1000,
                                                                         "approved_max_body_bytes": 1000,
                                                                         "streaming_upload": True})))

    def test_bounded_endpoint(self):
        endpoint = {"max_body_bytes": 1000, "approved_max_body_bytes": 2000,
                    "streaming_upload": False, "decompression_enabled": False}
        self.assertEqual([], audit(endpoint))


if __name__ == "__main__":
    unittest.main()
