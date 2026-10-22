import unittest
from agent import audit


class DatabaseReplicaLagAuditTests(unittest.TestCase):
    def test_replica_lag(self):
        self.assertTrue(any("lag" in f["issue"] for f in audit({"lag_seconds": 12, "max_lag_seconds": 5})))

    def test_healthy_replica(self):
        replica = {"lag_seconds": 1, "max_lag_seconds": 5, "replication_healthy": True,
                   "failover_eligible": False, "replay_queue_bytes": 0, "max_replay_queue_bytes": 100}
        self.assertEqual([], audit(replica))


if __name__ == "__main__":
    unittest.main()
