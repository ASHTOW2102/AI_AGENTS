import unittest
from agent import audit


class KubernetesHorizontalAutoscalerThrashAuditTests(unittest.TestCase):

    def test_thrashing(self):
        self.assertTrue(audit({"scale_events_per_hour": 30, "max_acceptable_scale_events_per_hour": 10}))

    def test_ok(self):
        self.assertFalse(audit({"scale_events_per_hour": 2, "max_acceptable_scale_events_per_hour": 10, "stabilization_window_configured": True}))
