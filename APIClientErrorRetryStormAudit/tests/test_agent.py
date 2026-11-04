import unittest
from agent import audit


class APIClientErrorRetryStormAuditTests(unittest.TestCase):

    def test_retries_on_4xx(self):
        self.assertTrue(audit({"retries_on_4xx": True}))

    def test_ok(self):
        self.assertFalse(audit({"retries_on_4xx": False, "retry_enabled": True, "jitter_applied": True, "circuit_breaker_coordinated": True}))
