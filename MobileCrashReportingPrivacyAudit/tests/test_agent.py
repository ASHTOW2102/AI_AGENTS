import unittest
from agent import audit


class MobileCrashReportingPrivacyAuditTests(unittest.TestCase):

    def test_unscrubbed(self):
        self.assertTrue(audit({"includes_raw_user_input": True, "scrubbed_before_send": False}))

    def test_ok(self):
        self.assertFalse(audit({"includes_raw_user_input": True, "scrubbed_before_send": True, "includes_device_identifiers": False}))
