import unittest

from agent import audit


class CloudFailoverReadinessAuditTests(unittest.TestCase):
    def test_flags_single_region_and_stale_exercise(self):
        self.assertEqual(2, len(audit({"regions": 1, "days_since_failover_exercise": 500})))

    def test_ready_service(self):
        service = {"regions": 2, "target_rto_minutes": 60, "measured_rto_minutes": 30,
                   "max_replication_lag_minutes": 5, "replication_lag_minutes": 1,
                   "days_since_failover_exercise": 60}
        self.assertEqual([], audit(service))


if __name__ == "__main__":
    unittest.main()
