import unittest
from agent import audit


class MobileAppPermissionCreepAuditTests(unittest.TestCase):

    def test_unjustified(self):
        self.assertTrue(audit({"requested_permissions": ["camera", "contacts"], "justified_permissions": ["camera"]}))

    def test_ok(self):
        self.assertFalse(audit({"requested_permissions": ["camera"], "justified_permissions": ["camera"], "requests_background_location": False}))
