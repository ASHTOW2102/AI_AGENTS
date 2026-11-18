import unittest
from agent import audit


class FeatureFlagApprovalWorkflowAuditTests(unittest.TestCase):

    def test_no_approval(self):
        self.assertTrue(audit({"risk_level": "high", "requires_approval_to_toggle": False}))

    def test_ok(self):
        self.assertFalse(audit({"risk_level": "high", "requires_approval_to_toggle": True, "approver_can_be_same_as_requester": False}))
