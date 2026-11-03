import unittest
from agent import audit


class APIFieldMaskAuditTests(unittest.TestCase):

    def test_sensitive_by_default(self):
        self.assertTrue(audit({"supports_field_mask": True, "sensitive_fields_excluded_by_default": False}))

    def test_ok(self):
        self.assertFalse(audit({"supports_field_mask": True, "sensitive_fields_excluded_by_default": True, "field_mask_injection_possible": False}))
