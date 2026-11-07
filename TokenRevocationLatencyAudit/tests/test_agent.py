import unittest
from agent import audit


class TokenRevocationLatencyAuditTests(unittest.TestCase):

    def test_slow_propagation(self):
        self.assertTrue(audit({"revocation_propagation_ms": 10000, "max_acceptable_propagation_ms": 5000}))

    def test_ok(self):
        self.assertFalse(audit({"revocation_propagation_ms": 100, "max_acceptable_propagation_ms": 5000, "revocation_checked_on_validate": True}))
