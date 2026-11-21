import unittest
from agent import audit


class FeatureFlagTelemetryGapAuditTests(unittest.TestCase):

    def test_no_telemetry(self):
        self.assertTrue(audit({"variant_exposure_logged": False}))

    def test_ok(self):
        self.assertFalse(audit({"variant_exposure_logged": True, "linked_to_success_metric": True}))
