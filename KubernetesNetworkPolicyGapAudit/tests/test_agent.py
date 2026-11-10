import unittest
from agent import audit


class KubernetesNetworkPolicyGapAuditTests(unittest.TestCase):

    def test_no_policy(self):
        self.assertTrue(audit({"default_deny_policy_present": False}))

    def test_ok(self):
        self.assertFalse(audit({"default_deny_policy_present": True, "unrestricted_egress": False}))
