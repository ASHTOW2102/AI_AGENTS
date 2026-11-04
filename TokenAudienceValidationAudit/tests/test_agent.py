import unittest
from agent import audit


class TokenAudienceValidationAuditTests(unittest.TestCase):

    def test_no_validation(self):
        self.assertTrue(audit({"validates_audience_claim": False}))

    def test_ok(self):
        self.assertFalse(audit({"validates_audience_claim": True, "accepts_wildcard_audience": False}))
