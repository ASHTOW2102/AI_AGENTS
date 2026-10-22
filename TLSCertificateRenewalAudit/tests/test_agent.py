import unittest
from datetime import date
from agent import audit


class TLSCertificateRenewalAuditTests(unittest.TestCase):
    def test_expired_certificate(self):
        self.assertEqual("critical", audit({"expires_on": "2024-01-01"}, date(2025, 1, 1))[0]["severity"])

    def test_current_certificate(self):
        cert = {"expires_on": "2027-01-01", "automated_renewal": True, "hostname_match": True}
        self.assertEqual([], audit(cert, date(2026, 1, 1)))


if __name__ == "__main__":
    unittest.main()
