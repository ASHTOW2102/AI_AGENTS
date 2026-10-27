import unittest
from agent import audit


class RPORecoveryPointAuditTests(unittest.TestCase):
    def test_backup_interval_misses_rpo(self):
        self.assertIn("cannot meet", audit({"backup_interval_minutes": 60, "target_rpo_minutes": 15})[0]["issue"])

    def test_meets_objective(self):
        service = {"measured_data_loss_minutes": 2, "target_rpo_minutes": 15,
                   "backup_interval_minutes": 10, "recovery_point_tested": True,
                   "replication_lag_minutes": 1}
        self.assertEqual([], audit(service))


if __name__ == "__main__":
    unittest.main()
