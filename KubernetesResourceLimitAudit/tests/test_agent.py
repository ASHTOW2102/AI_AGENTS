import unittest
from agent import audit


class KubernetesResourceLimitAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"containers": [{"name": "app", "cpu_limit": None, "memory_limit": "512Mi"}]}))

    def test_ok(self):
        self.assertFalse(audit({"containers": [{"name": "app", "cpu_limit": "500m", "memory_limit": "512Mi"}]}))
