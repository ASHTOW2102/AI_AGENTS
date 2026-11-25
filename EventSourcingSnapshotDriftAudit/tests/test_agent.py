import unittest
from agent import audit


class EventSourcingSnapshotDriftAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"snapshot_version": 2, "current_schema_version": 4}))

    def test_ok(self):
        self.assertFalse(audit({"snapshot_version": 4, "current_schema_version": 4}))
