import unittest
from agent import audit


class APIContentLengthAuditTests(unittest.TestCase):
    def test_unbounded_request(self):
        self.assertIn("no positive", audit({})[0]["issue"])

    def test_bounded_endpoint(self):
        endpoint = {"max_request_bytes": 1000, "approved_request_bytes": 2000,
                    "streaming_request": False, "max_response_bytes": 1000,
                    "approved_response_bytes": 2000}
        self.assertEqual([], audit(endpoint))


if __name__ == "__main__":
    unittest.main()
