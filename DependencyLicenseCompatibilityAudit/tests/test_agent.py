import unittest
from agent import audit


class DependencyLicenseCompatibilityAuditTests(unittest.TestCase):
    def test_disallowed_license(self):
        self.assertIn("not on the approved", audit({"license": "Unknown"}, {"MIT", "Apache-2.0"})[0]["issue"])

    def test_approved_license(self):
        self.assertEqual([], audit({"license": "MIT", "copyleft": False, "license_file_present": True}, {"MIT"}))


if __name__ == "__main__":
    unittest.main()
