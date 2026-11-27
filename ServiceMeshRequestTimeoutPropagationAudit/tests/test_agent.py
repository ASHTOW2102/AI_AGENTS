import unittest
from agent import audit


class ServiceMeshRequestTimeoutPropagationAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"caller_timeout_ms": 1000, "callee_timeout_ms": 1500}))

    def test_ok(self):
        self.assertFalse(audit({"caller_timeout_ms": 1000, "callee_timeout_ms": 500}))
