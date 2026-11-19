import unittest
from agent import audit


class DatabaseTriggerCascadeAuditTests(unittest.TestCase):

    def test_unbounded_cascade(self):
        self.assertTrue(audit({"can_trigger_other_triggers": True, "cascade_depth_limited": False}))

    def test_ok(self):
        self.assertFalse(audit({"can_trigger_other_triggers": True, "cascade_depth_limited": True, "fires_on_bulk_operations": True, "bulk_operation_performance_tested": True}))
