import unittest
from agent import audit


class ClockNTPReadinessAuditTests(unittest.TestCase):
    def test_excessive_drift(self):
        self.assertIn("drift", audit({"observed_drift_ms": 5000, "max_drift_ms": 1000})[0]["issue"])

    def test_synchronized_host(self):
        host = {"time_sync_enabled": True, "configured_sources": 3, "observed_drift_ms": 10,
                "max_drift_ms": 100, "last_sync_age_hours": 1, "max_sync_age_hours": 24}
        self.assertEqual([], audit(host))


if __name__ == "__main__":
    unittest.main()
