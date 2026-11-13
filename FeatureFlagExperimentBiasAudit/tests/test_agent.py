import unittest
from agent import audit


class FeatureFlagExperimentBiasAuditTests(unittest.TestCase):

    def test_srm(self):
        self.assertTrue(audit({"observed_sample_ratio": 0.6, "expected_sample_ratio": 0.5, "max_acceptable_srm_deviation": 0.05}))

    def test_ok(self):
        self.assertFalse(audit({"observed_sample_ratio": 0.5, "expected_sample_ratio": 0.5, "max_acceptable_srm_deviation": 0.05, "randomization_unit_consistent": True}))
