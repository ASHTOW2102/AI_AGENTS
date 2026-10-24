import unittest
from agent import audit


class DataPipelineBackfillAuditTests(unittest.TestCase):
    def test_non_idempotent_backfill(self):
        self.assertIn("safely resume", audit({"idempotent": False})[0]["issue"])

    def test_safe_plan(self):
        plan = {"estimated_rows": 1000, "max_rows_per_run": 500, "chunked": True,
                "checkpointing": True, "idempotent": True, "post_run_validation": True}
        self.assertEqual([], audit(plan))


if __name__ == "__main__":
    unittest.main()
