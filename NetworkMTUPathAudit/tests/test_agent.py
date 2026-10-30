import unittest
from agent import audit


class NetworkMTUPathAuditTests(unittest.TestCase):
    def test_interface_exceeds_path(self):
        self.assertIn("exceeds", audit({"interface_mtu": 9000, "path_mtu": 1500})[0]["issue"])

    def test_matched_mtu(self):
        path = {"interface_mtu": 1500, "path_mtu": 1500, "large_payloads_expected": True,
                "path_mtu_discovery_working": True, "fragmentation_observed": False,
                "mtu_monitoring_configured": True}
        self.assertEqual([], audit(path))


if __name__ == "__main__":
    unittest.main()
