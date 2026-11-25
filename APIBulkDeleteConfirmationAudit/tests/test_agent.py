import unittest
from agent import audit


class APIBulkDeleteConfirmationAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"supports_bulk_delete": True, "requires_confirmation_token": False}))

    def test_ok(self):
        self.assertFalse(audit({"supports_bulk_delete": True, "requires_confirmation_token": True}))
