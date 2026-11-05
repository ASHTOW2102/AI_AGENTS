import unittest
from agent import audit


class FeatureFlagDependencyAuditTests(unittest.TestCase):

    def test_self_cycle(self):
        self.assertTrue(audit({"name": "a", "depends_on": ["a"]}))

    def test_ok(self):
        self.assertFalse(audit({"name": "a", "depends_on": ["b"], "disabled_dependencies": [], "enabled": True, "dependency_validated_at_evaluation": True}))
