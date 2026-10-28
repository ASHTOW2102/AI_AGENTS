import unittest
from agent import audit


class CronJobOverlapAuditTests(unittest.TestCase):
    def test_unlocked_overlap(self):
        self.assertIn("overlap", audit({"runtime_p99_minutes": 20, "schedule_interval_minutes": 15})[0]["issue"])

    def test_safe_schedule(self):
        job = {"runtime_p99_minutes": 5, "schedule_interval_minutes": 15,
               "singleton_required": True, "distributed_lock": True,
               "missed_run_policy": "skip", "max_parallel_runs": 1, "approved_max_parallel_runs": 1}
        self.assertEqual([], audit(job))


if __name__ == "__main__":
    unittest.main()
