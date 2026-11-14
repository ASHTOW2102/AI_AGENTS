import unittest
from agent import audit


class APIClientCertRotationAuditTests(unittest.TestCase):

    def test_expiring_no_renewal(self):
        self.assertTrue(audit({"days_until_cert_expiry": 5, "renewal_warning_days": 14, "auto_renewal_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"days_until_cert_expiry": 60, "renewal_warning_days": 14, "auto_renewal_enabled": True, "cert_expiry_monitored": True}))
