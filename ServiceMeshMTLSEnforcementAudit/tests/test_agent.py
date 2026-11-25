import unittest
from agent import audit


class ServiceMeshMTLSEnforcementAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"mtls_mode": "PERMISSIVE"}))

    def test_ok(self):
        self.assertFalse(audit({"mtls_mode": "STRICT"}))
