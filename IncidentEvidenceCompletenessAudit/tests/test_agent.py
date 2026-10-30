import unittest
from agent import audit


class IncidentEvidenceCompletenessAuditTests(unittest.TestCase):
    def test_missing_impact(self):
        self.assertIn("impact summary", audit({})[1]["issue"])

    def test_complete_incident(self):
        incident = {"start_time": "t1", "impact_summary": "degraded", "root_cause": "dependency",
                    "resolution_time": "t2", "follow_up_actions": 0, "customer_impact": False}
        self.assertEqual([], audit(incident))


if __name__ == "__main__":
    unittest.main()
