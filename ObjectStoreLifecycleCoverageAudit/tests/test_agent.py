import unittest
from agent import audit


class ObjectStoreLifecycleCoverageAuditTests(unittest.TestCase):
    def test_stale_versions_without_expiry(self):
        self.assertIn("no expiry", audit({"noncurrent_versions_exist": True})[0]["issue"])

    def test_lifecycle_rules_present(self):
        bucket = {"noncurrent_versions_exist": True, "noncurrent_expiry_days": 30,
                  "temporary_prefixes": True, "temporary_expiry_days": 7,
                  "incomplete_multipart_uploads_possible": True, "multipart_abort_days": 3}
        self.assertEqual([], audit(bucket))


if __name__ == "__main__":
    unittest.main()
