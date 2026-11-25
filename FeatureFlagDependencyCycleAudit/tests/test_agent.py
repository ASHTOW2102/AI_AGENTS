import unittest
from agent import audit


class FeatureFlagDependencyCycleAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"dependencies": {"a": ["b"], "b": ["a"]}}))

    def test_ok(self):
        self.assertFalse(audit({"dependencies": {"a": ["b"], "b": []}}))
