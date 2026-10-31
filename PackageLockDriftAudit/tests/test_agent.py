import unittest
from agent import audit


class PackageLockDriftAuditTests(unittest.TestCase):
    def test_installed_lock_mismatch(self):
        self.assertIn("differs from lockfile", audit({"packages": [{"name": "lib", "installed_version": "2", "locked_version": "1"}]})[0]["issue"])

    def test_lock_matches(self):
        report = {"packages": [{"name": "lib", "installed_version": "1", "locked_version": "1",
                                 "floating_constraint": False}], "lockfile_out_of_date": False}
        self.assertEqual([], audit(report))


if __name__ == "__main__":
    unittest.main()
