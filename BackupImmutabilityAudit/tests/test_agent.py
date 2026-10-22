import unittest
from agent import audit


class BackupImmutabilityAuditTests(unittest.TestCase):
    def test_admin_overlap(self):
        self.assertIn("overlap", audit({"immutable": True, "delete_admins_overlap_production_admins": True})[0]["issue"])

    def test_protected_backup(self):
        backup = {"immutable": True, "immutability_days": 90, "required_immutability_days": 30,
                  "delete_admins_overlap_production_admins": False, "restore_tested": True}
        self.assertEqual([], audit(backup))


if __name__ == "__main__":
    unittest.main()
