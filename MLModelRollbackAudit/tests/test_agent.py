import unittest
from agent import audit


class MLModelRollbackAuditTests(unittest.TestCase):
    def test_missing_previous_artifact(self):
        self.assertIn("not retained", audit({})[0]["issue"])

    def test_rollback_ready(self):
        deployment = {"previous_model_artifact_retained": True, "rollback_route_tested": True,
                      "feature_schema_changed": False, "rollback_slo_minutes": 2,
                      "max_rollback_slo_minutes": 5}
        self.assertEqual([], audit(deployment))


if __name__ == "__main__":
    unittest.main()
