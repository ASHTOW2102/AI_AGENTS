import unittest
from agent import audit


class KubernetesServiceAccountTokenMountAuditTests(unittest.TestCase):

    def test_unused_mount(self):
        self.assertTrue(audit({"automount_service_account_token": True, "calls_kubernetes_api": False}))

    def test_ok(self):
        self.assertFalse(audit({"automount_service_account_token": False, "calls_kubernetes_api": False, "service_account": "scoped-sa"}))
