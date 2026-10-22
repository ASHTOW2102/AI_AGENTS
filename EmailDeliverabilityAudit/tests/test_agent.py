import unittest
from agent import audit


class EmailDeliverabilityAuditTests(unittest.TestCase):
    def test_missing_authentication(self):
        self.assertEqual(3, len(audit({"spf_valid": False, "dkim_valid": False, "dmarc_valid": False})))

    def test_authenticated_domain(self):
        domain = {"spf_valid": True, "dkim_valid": True, "dmarc_valid": True,
                  "dmarc_policy": "reject", "bounce_rate_percent": 1, "max_bounce_rate_percent": 5}
        self.assertEqual([], audit(domain))


if __name__ == "__main__":
    unittest.main()
