import unittest
from agent import audit


class CloudLoadBalancerHealthCheckAuditTests(unittest.TestCase):

    def test_generic_path(self):
        self.assertTrue(audit({"health_check_path": "/"}))

    def test_ok(self):
        self.assertFalse(audit({"health_check_path": "/healthz", "health_check_checks_downstream_dependency": False, "unhealthy_threshold": 3, "connection_draining_enabled": True}))
