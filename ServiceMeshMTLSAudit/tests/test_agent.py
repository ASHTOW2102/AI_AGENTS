import unittest
from agent import audit


class ServiceMeshMTLSAuditTests(unittest.TestCase):

    def test_non_strict(self):
        self.assertTrue(audit({"mesh_enabled": True, "mtls_strict_mode": False}))

    def test_ok(self):
        self.assertFalse(audit({"mesh_enabled": True, "mtls_strict_mode": True, "cert_age_days": 5, "cert_rotation_automated": True}))
