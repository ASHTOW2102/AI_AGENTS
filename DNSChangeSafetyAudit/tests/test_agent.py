import unittest
from agent import audit


class DNSChangeSafetyAuditTests(unittest.TestCase):
    def test_unreviewed_nameserver_change(self):
        self.assertIn("registrar", audit({"nameserver_change": True})[0]["issue"])

    def test_rehearsed_change(self):
        change = {"high_impact": True, "rollback_recorded": True, "nameserver_change": True,
                  "registrar_consistency_checked": True, "dnssec_enabled": False}
        self.assertEqual([], audit(change))


if __name__ == "__main__":
    unittest.main()
