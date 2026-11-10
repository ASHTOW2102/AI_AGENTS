import unittest
from agent import audit


class SearchAutocompleteInjectionAuditTests(unittest.TestCase):

    def test_unencoded(self):
        self.assertTrue(audit({"reflects_raw_input": True, "output_encoding_applied": False}))

    def test_ok(self):
        self.assertFalse(audit({"reflects_raw_input": True, "output_encoding_applied": True, "input_length_capped": True}))
