import unittest
from agent import audit


class TLSCertificateChainExpiryAuditTests(unittest.TestCase):
    def test_expired_chain(self):
        self.assertEqual("critical", audit({"days_until_expiry": -1})[0]["severity"])

    def test_valid_chain(self):
        cert = {"days_until_expiry": 200, "full_chain_served": True, "chain_validation_errors": 0}
        self.assertEqual([], audit(cert))


if __name__ == "__main__":
    unittest.main()
