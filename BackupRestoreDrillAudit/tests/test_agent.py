import unittest
from agent import audit


class BackupRestoreDrillAuditTests(unittest.TestCase):
    def test_incomplete_drill(self):
        findings = audit({"critical_datasets": 3, "datasets_restored": 1})
        self.assertTrue(any("all critical datasets" in f["issue"] for f in findings))

    def test_current_verified_drill(self):
        drill = {"days_since_last_restore": 20, "max_days_between_drills": 365,
                 "critical_datasets": 2, "datasets_restored": 2, "measured_rto_minutes": 30,
                 "target_rto_minutes": 60, "integrity_verified": True, "evidence_reference": "DR-9"}
        self.assertEqual([], audit(drill))


if __name__ == "__main__":
    unittest.main()
