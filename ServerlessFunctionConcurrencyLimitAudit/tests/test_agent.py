import unittest
from agent import audit


class ServerlessFunctionConcurrencyLimitAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"reserved_concurrency": 200, "downstream_connection_limit": 50}))

    def test_ok(self):
        self.assertFalse(audit({"reserved_concurrency": 20, "downstream_connection_limit": 50}))
