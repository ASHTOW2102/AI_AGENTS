import unittest
from agent import audit


class DisasterRecoveryExerciseAuditTests(unittest.TestCase):
    def test_missing_scenario(self):
        self.assertIn("database", audit({"required_scenarios": ["database"], "tested_scenarios": []})[0]["issue"])

    def test_successful_exercise(self):
        item = {"days_since_last_exercise": 20, "max_days_between_exercises": 365,
                "required_scenarios": ["region"], "tested_scenarios": ["region"],
                "measured_recovery_minutes": 10, "target_recovery_minutes": 30, "open_findings": 0}
        self.assertEqual([], audit(item))


if __name__ == "__main__":
    unittest.main()
