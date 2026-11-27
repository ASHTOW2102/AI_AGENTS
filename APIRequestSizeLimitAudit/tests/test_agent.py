import unittest
from agent import audit


class APIRequestSizeLimitAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"enforces_max_body_size": False}))

    def test_ok(self):
        self.assertFalse(audit({"enforces_max_body_size": True, "max_body_size_bytes": 1048576}))
