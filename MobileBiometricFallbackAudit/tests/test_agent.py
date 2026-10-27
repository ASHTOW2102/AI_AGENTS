import unittest
from agent import audit


class MobileBiometricFallbackAuditTests(unittest.TestCase):
    def test_biometric_data_leaves_device(self):
        self.assertEqual("critical", audit({"biometric_data_stays_on_device": False})[0]["severity"])

    def test_safe_policy(self):
        policy = {"biometrics_enabled": True, "device_credential_fallback": True,
                  "biometric_unlocks_sensitive_action": False, "biometric_data_stays_on_device": True}
        self.assertEqual([], audit(policy))


if __name__ == "__main__":
    unittest.main()
