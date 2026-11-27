import unittest
from agent import audit


class ContainerImageTagMutabilityAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"uses_latest_tag_in_production": True}))

    def test_ok(self):
        self.assertFalse(audit({"uses_latest_tag_in_production": False, "tag_immutability_enabled": True}))
