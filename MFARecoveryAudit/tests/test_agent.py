import unittest
from agent import audit


class MFARecoveryAuditTests(unittest.TestCase):
    def test_unsafe_support_reset(self):
        self.assertEqual("critical", audit({"support_can_disable_mfa": True})[0]["severity"])

    def test_safe_recovery(self):
        policy = {"mfa_required": True, "recovery_flow_tested": True,
                  "support_can_disable_mfa": False, "backup_codes_enabled": True,
                  "backup_codes_one_time": True, "recovery_bypasses_mfa": False}
        self.assertEqual([], audit(policy))


if __name__ == "__main__":
    unittest.main()
