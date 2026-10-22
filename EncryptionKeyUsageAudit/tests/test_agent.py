import unittest
from agent import audit


class EncryptionKeyUsageAuditTests(unittest.TestCase):
    def test_decommissioned_key_still_used(self):
        self.assertEqual("critical", audit({"decommissioned": True, "active_consumers": 1})[0]["severity"])

    def test_approved_key_policy(self):
        key = {"purposes": ["encrypt"], "algorithm": "AES-256", "approved_algorithms": ["AES-256"],
               "decommissioned": False, "active_consumers": 3, "exportable": False}
        self.assertEqual([], audit(key))


if __name__ == "__main__":
    unittest.main()
