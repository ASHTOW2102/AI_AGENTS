import unittest
from agent import audit


class KubernetesLivenessProbeAuditTests(unittest.TestCase):

    def test_no_probe(self):
        self.assertTrue(audit({"liveness_probe_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"liveness_probe_configured": True, "liveness_probe_checks_downstream_dependency": False, "initial_delay_seconds": 30, "startup_time_seconds": 10}))
