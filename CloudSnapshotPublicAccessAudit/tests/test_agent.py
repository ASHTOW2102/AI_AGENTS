import unittest
from agent import audit


class CloudSnapshotPublicAccessAuditTests(unittest.TestCase):
    def test_public_snapshot(self):
        self.assertEqual("critical", audit({"publicly_shared": True})[0]["severity"])

    def test_private_encrypted_snapshot(self):
        snapshot = {"publicly_shared": False, "cross_account_shared": False,
                    "sensitive_data": True, "encryption_confirmed": True,
                    "obsolete_days": 10, "max_obsolete_days": 90}
        self.assertEqual([], audit(snapshot))


if __name__ == "__main__":
    unittest.main()
