import unittest
from agent import audit


class LLMAgentLoopDetectionAuditTests(unittest.TestCase):

    def test_no_loop_detection(self):
        self.assertTrue(audit({"repeated_action_detection_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"repeated_action_detection_enabled": True, "max_steps_per_task_enforced": True}))
