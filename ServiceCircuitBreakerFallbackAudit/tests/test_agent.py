import unittest
from agent import audit


class ServiceCircuitBreakerFallbackAuditTests(unittest.TestCase):

    def test_no_fallback(self):
        self.assertTrue(audit({"circuit_breaker_enabled": True, "fallback_defined": False}))

    def test_ok(self):
        self.assertFalse(audit({"circuit_breaker_enabled": True, "fallback_defined": True, "fallback_returns_cached_data": False}))
