import unittest
from agent import audit


class MobileAppStoreReviewPermissionAuditTests(unittest.TestCase):

    def test_undeclared_permission(self):
        self.assertTrue(audit({"requested_permissions": ["camera"], "declared_purposes": {}}))

    def test_ok(self):
        self.assertFalse(audit({"requested_permissions": ["camera"], "declared_purposes": {"camera": "scan"}, "background_location_requested": False}))
