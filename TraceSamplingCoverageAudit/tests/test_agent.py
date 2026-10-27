import unittest
from agent import audit


class TraceSamplingCoverageAuditTests(unittest.TestCase):
    def test_sensitive_attributes(self):
        self.assertIn("Sensitive", audit({"sensitive_attributes_allowed": True})[0]["issue"])

    def test_compliant_sampling(self):
        policy = {"error_sampling_rate_percent": 100, "minimum_error_sampling_rate_percent": 100,
                  "head_sampling_rate_percent": 10, "max_head_sampling_rate_percent": 20,
                  "trace_id_propagation": True, "sensitive_attributes_allowed": False}
        self.assertEqual([], audit(policy))


if __name__ == "__main__":
    unittest.main()
