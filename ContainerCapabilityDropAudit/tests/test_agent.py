import unittest
from agent import audit


class ContainerCapabilityDropAuditTests(unittest.TestCase):

    def test_no_drop(self):
        self.assertTrue(audit({"capabilities_dropped": False}))

    def test_ok(self):
        self.assertFalse(audit({"capabilities_dropped": True, "retained_capabilities": [], "net_admin_justified": False}))
