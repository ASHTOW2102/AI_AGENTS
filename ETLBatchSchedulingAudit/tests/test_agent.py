import unittest
from agent import audit


class ETLBatchSchedulingAuditTests(unittest.TestCase):

    def test_missing_dependency_wait(self):
        self.assertTrue(audit({"depends_on": ["x"], "dependency_wait_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"expected_duration_minutes": 10, "schedule_window_minutes": 30}))
