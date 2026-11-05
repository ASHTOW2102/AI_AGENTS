import unittest
from agent import audit


class BackupRetentionLegalHoldAuditTests(unittest.TestCase):

    def test_hold_not_excluded(self):
        self.assertTrue(audit({"legal_hold_active": True, "eligible_for_scheduled_deletion": True}))

    def test_ok(self):
        self.assertFalse(audit({"legal_hold_active": True, "eligible_for_scheduled_deletion": False, "legal_hold_reference": "case-1"}))
