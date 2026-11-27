import unittest
from agent import audit


class CloudAutoScalingPolicyAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"min_capacity": 2, "max_capacity": 2}))

    def test_ok(self):
        self.assertFalse(audit({"min_capacity": 2, "max_capacity": 10}))
