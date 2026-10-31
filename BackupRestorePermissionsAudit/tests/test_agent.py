import unittest
from agent import audit


class BackupRestorePermissionsAuditTests(unittest.TestCase):
    def test_restore_delete_admin_overlap(self):
        self.assertIn("also delete", audit({"restore_admins_overlap_delete_admins": True})[0]["issue"])

    def test_separated_permissions(self):
        policy = {"restore_permission_count": 2, "approved_restore_permission_count": 3,
                  "restore_admins_overlap_delete_admins": False,
                  "restore_to_production_allowed": True, "restore_requires_approval": True,
                  "restore_activity_logged": True}
        self.assertEqual([], audit(policy))


if __name__ == "__main__":
    unittest.main()
