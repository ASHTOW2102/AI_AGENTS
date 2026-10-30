import unittest
from agent import audit


class DatabaseBackupConsistencyAuditTests(unittest.TestCase):
    def test_inconsistent_multi_volume_backup(self):
        self.assertIn("snapshot group", audit({"multi_volume": True, "snapshot_group_consistent": False})[0]["issue"])

    def test_validated_backup(self):
        backup = {"multi_volume": True, "snapshot_group_consistent": True,
                  "transactional_database": True, "log_position_recorded": True,
                  "integrity_check_passed": True, "restore_tested": True}
        self.assertEqual([], audit(backup))


if __name__ == "__main__":
    unittest.main()
