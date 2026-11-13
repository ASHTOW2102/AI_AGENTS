import unittest
from agent import audit


class ContainerRootlessRuntimeAuditTests(unittest.TestCase):

    def test_root_no_rootless(self):
        self.assertTrue(audit({"runs_as_root": True, "rootless_runtime_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"runs_as_root": False, "rootless_runtime_enabled": True, "uid_mapping": "offset"}))
