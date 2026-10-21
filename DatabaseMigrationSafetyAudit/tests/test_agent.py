import unittest
from agent import audit


class DatabaseMigrationSafetyAuditTests(unittest.TestCase):
    def test_destructive_migration_needs_backup(self):
        self.assertEqual("critical", audit({"destructive": True})[0]["severity"])

    def test_safe_rehearsed_migration(self):
        item = {"destructive": True, "backup_verified": True, "estimated_lock_seconds": 2,
                "max_lock_seconds": 10, "staging_rehearsed": True}
        self.assertEqual([], audit(item))


if __name__ == "__main__":
    unittest.main()
