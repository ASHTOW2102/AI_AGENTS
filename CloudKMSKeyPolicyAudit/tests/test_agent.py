import unittest
from agent import audit


class CloudKMSKeyPolicyAuditTests(unittest.TestCase):
    def test_admin_reader_overlap(self):
        self.assertIn("also have access", audit({"key_admins_overlap_data_readers": True})[0]["issue"])

    def test_restricted_key(self):
        key = {"rotation_enabled": True, "key_admins_overlap_data_readers": False,
               "decrypt_permission_principal_count": 2, "max_decrypt_principals": 5,
               "disabled": False, "active_dependents": 0}
        self.assertEqual([], audit(key))


if __name__ == "__main__":
    unittest.main()
