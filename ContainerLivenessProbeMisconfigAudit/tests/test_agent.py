import unittest
from agent import audit


class ContainerLivenessProbeMisconfigAuditTests(unittest.TestCase):

    def test_too_tight(self):
        self.assertTrue(audit({"liveness_timeout_seconds": 1, "p99_response_time_seconds": 3}))

    def test_ok(self):
        self.assertFalse(audit({"liveness_timeout_seconds": 10, "p99_response_time_seconds": 3, "liveness_probe_configured": True}))
