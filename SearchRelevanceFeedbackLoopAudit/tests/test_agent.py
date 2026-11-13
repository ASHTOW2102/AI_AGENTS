import unittest
from agent import audit


class SearchRelevanceFeedbackLoopAuditTests(unittest.TestCase):

    def test_uncorrected(self):
        self.assertTrue(audit({"trains_on_click_data": True, "position_bias_correction_applied": False}))

    def test_ok(self):
        self.assertFalse(audit({"trains_on_click_data": True, "position_bias_correction_applied": True, "feedback_loop_monitored": True}))
