import unittest
from agent import audit


class ProductionReadinessEvidenceAuditTests(unittest.TestCase):
    def test_migration_without_recovery(self):
        self.assertTrue(any("recovery plan" in f["issue"] for f in audit({"data_migration": True})))

    def test_complete_release(self):
        release = {"rollback_plan": "RB-1", "runbook": "RUN-1", "owner": "team",
                   "health_checks": True, "data_migration": False, "known_critical_findings": 0}
        self.assertEqual([], audit(release))


if __name__ == "__main__":
    unittest.main()
