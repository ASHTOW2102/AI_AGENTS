import unittest
from agent import audit


class BackupScheduleCoverageAuditTests(unittest.TestCase):
    def test_critical_without_schedule(self):
        self.assertEqual("critical", audit({"critical": True})[0]["severity"])

    def test_current_backup_plan(self):
        system = {"critical": True, "backup_schedule": "daily", "backup_interval_hours": 24,
                  "max_backup_interval_hours": 24, "retention_days": 90,
                  "minimum_retention_days": 30, "last_backup_success": True}
        self.assertEqual([], audit(system))


if __name__ == "__main__":
    unittest.main()
