import unittest
from agent import audit


class DataMaskingCoverageAuditTests(unittest.TestCase):

    def test_unmasked_in_staging(self):
        self.assertTrue(audit({"sensitive_fields": ["ssn"], "masked_fields": [], "tier": "staging"}))

    def test_ok(self):
        self.assertFalse(audit({"sensitive_fields": ["ssn"], "masked_fields": ["ssn"], "tier": "staging", "masking_applied": True, "masking_reversible": False}))
