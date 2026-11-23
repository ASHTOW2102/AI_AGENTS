import unittest
from agent import audit


class CICDArtifactSigningAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"publishes_to_public_registry": True, "artifact_signing_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"publishes_to_public_registry": True, "artifact_signing_enabled": True}))
