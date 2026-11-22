import unittest
from agent import audit


class LoadBalancerHealthCheckAuditTests(unittest.TestCase):

    def test_tcp_only(self):
        self.assertTrue(audit({"health_check_type": "tcp", "health_check_verifies_dependencies": False}))

    def test_ok(self):
        self.assertFalse(audit({"health_check_type": "http", "health_check_verifies_dependencies": True}))
