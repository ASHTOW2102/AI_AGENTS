import unittest
from agent import audit


class ServiceMeshMTLSCoverageAuditTests(unittest.TestCase):

    def test_gap(self):
        self.assertTrue(audit({"total_services": 10, "mtls_covered_services": 7}))

    def test_ok(self):
        self.assertFalse(audit({"total_services": 10, "mtls_covered_services": 10, "permissive_mode_enabled": False}))
