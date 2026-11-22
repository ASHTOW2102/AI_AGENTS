import unittest
from agent import audit


class EdgeFunctionColdStartAuditTests(unittest.TestCase):

    def test_slow_cold_start_no_mitigation(self):
        self.assertTrue(audit({"p99_cold_start_ms": 2500, "uses_provisioned_concurrency": False, "uses_warm_pool": False}))

    def test_ok(self):
        self.assertFalse(audit({"p99_cold_start_ms": 2500, "uses_provisioned_concurrency": True, "fetches_remote_config_synchronously_on_init": False}))
