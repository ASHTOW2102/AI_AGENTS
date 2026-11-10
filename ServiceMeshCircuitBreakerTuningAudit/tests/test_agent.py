import unittest
from agent import audit


class ServiceMeshCircuitBreakerTuningAuditTests(unittest.TestCase):

    def test_missing(self):
        self.assertTrue(audit({"circuit_breaker_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"circuit_breaker_configured": True, "consecutive_errors_threshold": 3, "recommended_max_threshold": 5}))
