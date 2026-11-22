import unittest
from agent import audit


class CertificateTransparencyMonitoringAuditTests(unittest.TestCase):

    def test_no_monitoring(self):
        self.assertTrue(audit({"monitors_ct_logs": False, "has_caa_record": False}))

    def test_ok(self):
        self.assertFalse(audit({"monitors_ct_logs": True, "has_caa_record": True}))
