import unittest
from agent import audit


class StorageReplicationAuditTests(unittest.TestCase):
    def test_required_replication_disabled(self):
        self.assertIn("disabled", audit({"replication_required": True, "replication_enabled": False})[0]["issue"])

    def test_healthy_replication(self):
        bucket = {"replication_required": True, "replication_enabled": True,
                  "replication_status_monitored": True, "replication_lag_minutes": 1,
                  "max_replication_lag_minutes": 5}
        self.assertEqual([], audit(bucket))


if __name__ == "__main__":
    unittest.main()
