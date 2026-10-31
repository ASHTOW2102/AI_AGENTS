import unittest
from agent import audit


class NetworkIngressAllowlistAuditTests(unittest.TestCase):
    def test_public_admin_port(self):
        self.assertEqual("critical", audit({"admin_ports_publicly_reachable": True})[0]["severity"])

    def test_restricted_rules(self):
        ruleset = {"world_open_rules": 0, "admin_ports_publicly_reachable": False,
                   "temporary_rules": 0, "ingress_change_auditing": True}
        self.assertEqual([], audit(ruleset))


if __name__ == "__main__":
    unittest.main()
