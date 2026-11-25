import unittest
from agent import audit


class QueueMessageVisibilityTimeoutAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"visibility_timeout_s": 30, "max_processing_time_s": 60}))

    def test_ok(self):
        self.assertFalse(audit({"visibility_timeout_s": 90, "max_processing_time_s": 60}))
