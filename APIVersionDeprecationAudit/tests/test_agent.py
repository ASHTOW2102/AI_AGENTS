import unittest
from agent import audit


class APIVersionDeprecationAuditTests(unittest.TestCase):

    def test_no_sunset_header(self):
        self.assertTrue(audit({"deprecated": True, "active_traffic": 100, "sunset_header_present": False}))

    def test_ok(self):
        self.assertFalse(audit({"deprecated": True, "active_traffic": 10, "sunset_header_present": True, "sunset_date": "2027-01-01"}))
