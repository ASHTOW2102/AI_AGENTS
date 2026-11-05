import unittest
from agent import audit


class ContainerLayerCacheAuditTests(unittest.TestCase):

    def test_secret_in_layer(self):
        self.assertTrue(audit({"secret_used_in_build": True, "secret_mount_type_used": False}))

    def test_ok(self):
        self.assertFalse(audit({"dependency_install_after_source_copy": False, "secret_used_in_build": False}))
