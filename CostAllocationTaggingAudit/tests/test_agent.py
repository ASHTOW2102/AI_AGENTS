import unittest
from agent import audit


class CostAllocationTaggingAuditTests(unittest.TestCase):

    def test_missing_tags(self):
        self.assertTrue(audit({"tags": {"owner": "x"}}))

    def test_ok(self):
        self.assertFalse(audit({"tags": {"owner": "x", "cost_center": "y", "environment": "prod"}}))
