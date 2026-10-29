import unittest
from agent import audit


class ObjectVersioningAuditTests(unittest.TestCase):
    def test_required_versioning_disabled(self):
        self.assertIn("disabled", audit({"versioning_required": True})[0]["issue"])

    def test_managed_versions(self):
        bucket = {"versioning_required": True, "versioning_enabled": True,
                  "delete_marker_recovery_tested": True, "noncurrent_version_lifecycle": True,
                  "critical_data": False}
        self.assertEqual([], audit(bucket))


if __name__ == "__main__":
    unittest.main()
