import unittest
from agent import audit


class APIVersionDeprecationHeaderAuditTests(unittest.TestCase):

    def test_missing_headers(self):
        self.assertTrue(audit({"deprecated": True, "headers": {}}))

    def test_ok(self):
        self.assertFalse(audit({"deprecated": True, "headers": {"Deprecation": "true", "Sunset": "x", "Link": "y"}}))
