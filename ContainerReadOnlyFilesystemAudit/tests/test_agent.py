import unittest
from agent import audit


class ContainerReadOnlyFilesystemAuditTests(unittest.TestCase):
    def test_writable_root(self):
        self.assertIn("root filesystem is writable", audit({"root_filesystem_read_only": False})[0]["issue"])

    def test_restricted_filesystem(self):
        container = {"root_filesystem_read_only": True, "read_only_root_filesystem": True,
                     "write_paths_required": False, "host_path_mounts": 0,
                     "writable_mount_count": 1, "approved_writable_mount_count": 1}
        self.assertEqual([], audit(container))


if __name__ == "__main__":
    unittest.main()
