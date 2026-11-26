import unittest
from agent import audit


class APISchemaVersioningAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"has_breaking_change": True, "version_bumped": False}))

    def test_ok(self):
        self.assertFalse(audit({"has_breaking_change": True, "version_bumped": True}))
