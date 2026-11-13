import unittest
from agent import audit


class ServerlessEventSourceThrottleAuditTests(unittest.TestCase):

    def test_no_limit(self):
        self.assertTrue(audit({"max_concurrency_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"max_concurrency_configured": True, "downstream_max_connections": 100, "configured_max_concurrency": 50}))
