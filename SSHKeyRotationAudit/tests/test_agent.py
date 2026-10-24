import unittest
from agent import audit


class SSHKeyRotationAuditTests(unittest.TestCase):
    def test_inactive_owner_key(self):
        self.assertTrue(any("inactive owner" in f["issue"] for f in audit({"owner": "old-user", "owner_active": False})))

    def test_current_key(self):
        key = {"age_days": 30, "max_age_days": 365, "owner": "ops", "owner_active": True,
               "revoked": False, "privileged": False}
        self.assertEqual([], audit(key))


if __name__ == "__main__":
    unittest.main()
