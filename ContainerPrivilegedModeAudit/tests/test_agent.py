import unittest
from agent import audit


class ContainerPrivilegedModeAuditTests(unittest.TestCase):

    def test_privileged(self):
        self.assertTrue(audit({"privileged": True}))

    def test_ok(self):
        self.assertFalse(audit({"privileged": False, "host_network": False, "host_pid": False}))
