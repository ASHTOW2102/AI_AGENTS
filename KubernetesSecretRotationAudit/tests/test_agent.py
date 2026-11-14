import unittest
from agent import audit


class KubernetesSecretRotationAuditTests(unittest.TestCase):

    def test_stale(self):
        self.assertTrue(audit({"age_days": 200, "max_acceptable_age_days": 90}))

    def test_ok(self):
        self.assertFalse(audit({"age_days": 5, "max_acceptable_age_days": 90, "automated_rotation_enabled": True}))
