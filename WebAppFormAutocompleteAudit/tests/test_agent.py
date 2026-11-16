import unittest
from agent import audit


class WebAppFormAutocompleteAuditTests(unittest.TestCase):

    def test_autocomplete_on(self):
        self.assertTrue(audit({"sensitive_fields": ["card_number"], "autocomplete_off_fields": []}))

    def test_ok(self):
        self.assertFalse(audit({"sensitive_fields": ["card_number"], "autocomplete_off_fields": ["card_number"], "is_shared_device_context": False}))
