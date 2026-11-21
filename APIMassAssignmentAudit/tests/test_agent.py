import unittest
from agent import audit


class APIMassAssignmentAuditTests(unittest.TestCase):

    def test_protected_bindable(self):
        self.assertTrue(audit({"protected_fields": ["is_admin"], "allowlisted_bindable_fields": [], "binds_request_body_directly": True}))

    def test_ok(self):
        self.assertFalse(audit({"protected_fields": ["is_admin"], "allowlisted_bindable_fields": ["name", "email"], "binds_request_body_directly": True}))
