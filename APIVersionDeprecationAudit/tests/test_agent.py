import unittest
from agent import audit


class APIVersionDeprecationAuditTests(unittest.TestCase):

    def test_deprecated_no_sunset(self):
        self.assertTrue(audit({"is_deprecated_version": True, "sends_sunset_header": False, "sunset_date": None}))

    def test_ok(self):
        self.assertFalse(audit({"is_deprecated_version": True, "sends_sunset_header": True, "sunset_date": "2027-01-01"}))
