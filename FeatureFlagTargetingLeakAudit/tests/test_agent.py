import unittest
from agent import audit


class FeatureFlagTargetingLeakAuditTests(unittest.TestCase):

    def test_leaked_segments(self):
        self.assertTrue(audit({"targeting_rules_shipped_to_client": True, "contains_internal_segment_names": True}))

    def test_ok(self):
        self.assertFalse(audit({"targeting_rules_shipped_to_client": True, "contains_internal_segment_names": False, "flag_name_reveals_unreleased_feature": False, "shipped_to_client": True}))
