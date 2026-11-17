import unittest
from agent import audit


class DataAnonymizationReversibilityAuditTests(unittest.TestCase):

    def test_unsalted(self):
        self.assertTrue(audit({"anonymization_method": "deterministic_hash", "salted": False}))

    def test_ok(self):
        self.assertFalse(audit({"anonymization_method": "deterministic_hash", "salted": True, "k_anonymity_evaluated": True}))
