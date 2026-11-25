import unittest
from agent import audit


class LoadBalancerSSLTerminationAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"terminates_ssl_at_lb": True, "backend_traffic_encrypted": False}))

    def test_ok(self):
        self.assertFalse(audit({"terminates_ssl_at_lb": True, "backend_traffic_encrypted": True}))
