import unittest
from agent import audit


class APISunsetHeaderAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"is_deprecated": True, "has_sunset_header": False}))

    def test_ok(self):
        self.assertFalse(audit({"is_deprecated": True, "has_sunset_header": True}))
