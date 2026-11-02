import unittest
from agent import audit


class APICursorStabilityAuditTests(unittest.TestCase):

    def test_offset_cursor(self):
        self.assertTrue(audit({"cursor_based": True, "cursor_field": "offset"}))

    def test_ok(self):
        self.assertFalse(audit({"cursor_based": True, "cursor_field": "id", "cursor_tie_breaker": "id"}))
