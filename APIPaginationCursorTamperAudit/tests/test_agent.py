import unittest
from agent import audit


class APIPaginationCursorTamperAuditTests(unittest.TestCase):

    def test_unsigned(self):
        self.assertTrue(audit({"cursor_format": "plain", "cursor_signed": False}))

    def test_ok(self):
        self.assertFalse(audit({"cursor_format": "plain", "cursor_signed": True, "cursor_encodes_internal_ids": False}))
