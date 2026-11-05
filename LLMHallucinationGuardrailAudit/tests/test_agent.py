import unittest
from agent import audit


class LLMHallucinationGuardrailAuditTests(unittest.TestCase):

    def test_no_groundedness_check(self):
        self.assertTrue(audit({"answers_from_retrieval": True, "groundedness_check_applied": False}))

    def test_ok(self):
        self.assertFalse(audit({"answers_from_retrieval": True, "groundedness_check_applied": True, "fallback_on_low_groundedness": True, "high_stakes_domain": False}))
