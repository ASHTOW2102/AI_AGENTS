import unittest
from agent import audit


class FeatureFlagMultiTenantIsolationAuditTests(unittest.TestCase):

    def test_global_leak(self):
        self.assertTrue(audit({"evaluation_scope": "global", "intended_scope": "per_tenant"}))

    def test_ok(self):
        self.assertFalse(audit({"evaluation_scope": "per_tenant", "intended_scope": "per_tenant", "tenant_id_validated_at_evaluation": True}))
