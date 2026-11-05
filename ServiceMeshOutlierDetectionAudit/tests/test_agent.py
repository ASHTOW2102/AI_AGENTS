import unittest
from agent import audit


class ServiceMeshOutlierDetectionAuditTests(unittest.TestCase):

    def test_no_detection(self):
        self.assertTrue(audit({"outlier_detection_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"outlier_detection_enabled": True, "consecutive_errors_threshold": 5, "ejected_endpoint_count": 1, "total_endpoint_count": 10}))
