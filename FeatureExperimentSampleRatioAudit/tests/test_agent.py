import unittest
from agent import audit


class FeatureExperimentSampleRatioAuditTests(unittest.TestCase):

    def test_ratio_mismatch(self):
        self.assertTrue(audit({"observed_ratio": 0.7, "expected_ratio": 0.5, "max_deviation_fraction": 0.05}))

    def test_ok(self):
        self.assertFalse(audit({"observed_ratio": 0.51, "expected_ratio": 0.5, "max_deviation_fraction": 0.1, "sample_size": 1000, "min_sample_size_for_power": 500}))
