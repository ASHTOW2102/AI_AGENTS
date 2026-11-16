import unittest
from agent import audit


class CloudResourceTaggingAuditTests(unittest.TestCase):

    def test_missing_tags(self):
        self.assertTrue(audit({"tags": {"owner": "team-a"}}))

    def test_ok(self):
        self.assertFalse(audit({"tags": {"owner": "team-a", "cost_center": "cc1", "environment": "staging"}}))
