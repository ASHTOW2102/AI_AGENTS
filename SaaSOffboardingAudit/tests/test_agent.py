import unittest
from agent import audit


class SaaSOffboardingAuditTests(unittest.TestCase):
    def test_credentials_not_revoked(self):
        self.assertEqual("critical", audit({"contract_terminated": True, "credentials_revoked": False})[0]["severity"])

    def test_complete_offboarding(self):
        vendor = {"contract_terminated": True, "active_accounts": 0, "credentials_revoked": True,
                  "data_return_required": True, "data_return_confirmed": True,
                  "data_deletion_required": True, "deletion_certificate_received": True}
        self.assertEqual([], audit(vendor))


if __name__ == "__main__":
    unittest.main()
