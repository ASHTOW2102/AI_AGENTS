import unittest
from agent import audit


class ContainerImageSizeAuditTests(unittest.TestCase):

    def test_oversized(self):
        self.assertTrue(audit({"size_mb": 1200, "max_acceptable_size_mb": 500}))

    def test_ok(self):
        self.assertFalse(audit({"size_mb": 80, "max_acceptable_size_mb": 500, "uses_full_os_base_image": False}))
