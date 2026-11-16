import unittest
from agent import audit


class NetworkPortScanDetectionAuditTests(unittest.TestCase):

    def test_no_detection(self):
        self.assertTrue(audit({"port_scan_detection_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"port_scan_detection_enabled": True, "detection_to_alert_latency_seconds": 30, "max_acceptable_latency_seconds": 300}))
