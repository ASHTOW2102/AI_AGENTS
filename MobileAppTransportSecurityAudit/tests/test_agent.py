import unittest
from agent import audit


class MobileAppTransportSecurityAuditTests(unittest.TestCase):
    def test_trust_all_certificates(self):
        self.assertEqual("critical", audit({"trust_all_certificates": True})[0]["severity"])

    def test_secure_release(self):
        app = {"cleartext_traffic_enabled": False, "trust_all_certificates": False,
               "debug_trust_override_in_release": False, "exception_domains": []}
        self.assertEqual([], audit(app))


if __name__ == "__main__":
    unittest.main()
