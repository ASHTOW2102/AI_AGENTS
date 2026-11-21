import unittest
from agent import audit


class ContainerReadOnlyRootFilesystemAuditTests(unittest.TestCase):

    def test_unnecessarily_writable(self):
        self.assertTrue(audit({"root_filesystem_readonly": False, "requires_root_writes": False}))

    def test_ok(self):
        self.assertFalse(audit({"root_filesystem_readonly": True, "requires_root_writes": False, "tmp_mounted_as_tmpfs": True}))
