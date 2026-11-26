import unittest
from agent import audit


class ServiceMeshCircuitBreakerAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"circuit_breaker_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"circuit_breaker_configured": True}))
