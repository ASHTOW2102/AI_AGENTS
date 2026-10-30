import unittest
from agent import audit


class MLModelCalibrationAuditTests(unittest.TestCase):
    def test_error_above_limit(self):
        self.assertIn("exceeds", audit({"calibration_metric_available": True,
                                        "expected_calibration_error": 0.3,
                                        "max_expected_calibration_error": 0.1})[0]["issue"])

    def test_calibrated_model(self):
        report = {"calibration_metric_available": True, "expected_calibration_error": 0.02,
                  "max_expected_calibration_error": 0.1, "decision_threshold": 0.7,
                  "threshold_validated": True, "days_since_calibration_review": 10,
                  "max_review_age_days": 180}
        self.assertEqual([], audit(report))


if __name__ == "__main__":
    unittest.main()
