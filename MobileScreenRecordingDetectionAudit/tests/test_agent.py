import unittest
from agent import audit


class MobileScreenRecordingDetectionAuditTests(unittest.TestCase):

    def test_undetected(self):
        self.assertTrue(audit({"displays_sensitive_data": True, "screen_recording_detection_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"displays_sensitive_data": True, "screen_recording_detection_enabled": True, "blur_on_detection": True}))
