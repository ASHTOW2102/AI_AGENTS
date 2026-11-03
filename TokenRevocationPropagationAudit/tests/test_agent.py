import unittest
from agent import audit


class TokenRevocationPropagationAuditTests(unittest.TestCase):

    def test_slow_propagation(self):
        self.assertTrue(audit({"revocation_propagation_seconds": 300, "max_acceptable_propagation_seconds": 60}))

    def test_ok(self):
        self.assertFalse(audit({"revocation_propagation_seconds": 10, "max_acceptable_propagation_seconds": 60, "token_type": "opaque"}))
