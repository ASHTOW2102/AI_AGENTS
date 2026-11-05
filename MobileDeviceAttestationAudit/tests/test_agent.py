import unittest
from agent import audit


class MobileDeviceAttestationAuditTests(unittest.TestCase):

    def test_no_attestation(self):
        self.assertTrue(audit({"operation_sensitive": True, "device_attestation_checked": False}))

    def test_ok(self):
        self.assertFalse(audit({"operation_sensitive": True, "device_attestation_checked": True, "device_rooted_or_jailbroken": False, "operation_allowed": True, "attestation_token_cached_minutes": 10, "max_attestation_cache_minutes": 60}))
