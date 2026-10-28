import unittest
from agent import audit


class DBConnectionTLSAuditTests(unittest.TestCase):
    def test_no_tls(self):
        self.assertEqual("critical", audit({"tls_enabled": False})[0]["severity"])

    def test_verified_tls(self):
        connection = {"tls_enabled": True, "certificate_validation": True, "min_tls_version": "TLS1.2"}
        self.assertEqual([], audit(connection))


if __name__ == "__main__":
    unittest.main()
