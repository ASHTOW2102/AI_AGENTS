import unittest
from agent import audit


class KubernetesAdmissionControllerAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"pod_security_admission_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"pod_security_admission_enabled": True}))
