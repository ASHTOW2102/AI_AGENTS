import unittest
from agent import audit


class ServiceMeshTrafficMirroringAuditTests(unittest.TestCase):

    def test_unsanitized(self):
        self.assertTrue(audit({"mirrors_to_nonprod": True, "payload_sanitized": False}))

    def test_ok(self):
        self.assertFalse(audit({"mirrors_to_nonprod": True, "payload_sanitized": True, "mirroring_percentage_capped": True}))
