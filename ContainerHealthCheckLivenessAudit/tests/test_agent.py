import unittest
from agent import audit


class ContainerHealthCheckLivenessAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"liveness_probe_configured": False, "readiness_probe_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"liveness_probe_configured": True, "readiness_probe_configured": True}))
