import unittest
from agent import audit


class ModelRegistryGovernanceAuditTests(unittest.TestCase):

    def test_no_approver(self):
        self.assertTrue(audit({"stage": "production", "approved_by": None}))

    def test_ok(self):
        self.assertFalse(audit({"stage": "staging", "training_data_reference": "x"}))
