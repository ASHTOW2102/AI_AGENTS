import unittest
from agent import audit


class DataShareExternalPartyAuditTests(unittest.TestCase):

    def test_no_dpa(self):
        self.assertTrue(audit({"shared_externally": True, "dpa_signed": False}))

    def test_ok(self):
        self.assertFalse(audit({"shared_externally": True, "dpa_signed": True, "access_expiry_date": "2027-01-01"}))
