import unittest
from agent import audit


class CloudLoadBalancerTLSVersionAuditTests(unittest.TestCase):

    def test_old_tls(self):
        self.assertTrue(audit({"allowed_tls_versions": ["TLSv1.0", "TLSv1.2"]}))

    def test_ok(self):
        self.assertFalse(audit({"allowed_tls_versions": ["TLSv1.2", "TLSv1.3"], "hsts_enabled": True}))
