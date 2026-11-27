import unittest
from agent import audit


class WebAppHSTSPreloadAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"hsts_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"hsts_enabled": True, "hsts_max_age_seconds": 63072000}))
