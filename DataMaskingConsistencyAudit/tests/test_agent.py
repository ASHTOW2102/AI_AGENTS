import unittest
from agent import audit


class DataMaskingConsistencyAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"requires_join_consistency": True, "masking_is_deterministic": False}))

    def test_ok(self):
        self.assertFalse(audit({"requires_join_consistency": True, "masking_is_deterministic": True}))
