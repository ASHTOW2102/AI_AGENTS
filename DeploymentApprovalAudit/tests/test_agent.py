import unittest
from agent import audit


class DeploymentApprovalAuditTests(unittest.TestCase):
    def test_unapproved_production_change(self):
        self.assertTrue(any("approval reference" in f["issue"] for f in audit({"production": True})))

    def test_approved_deployment(self):
        deployment = {"production": True, "approval_reference": "CHG-1", "deployer": "alice",
                      "approver": "bob", "change_window_required": False}
        self.assertEqual([], audit(deployment))


if __name__ == "__main__":
    unittest.main()
