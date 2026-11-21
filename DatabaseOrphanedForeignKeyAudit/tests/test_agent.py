import unittest
from agent import audit


class DatabaseOrphanedForeignKeyAuditTests(unittest.TestCase):

    def test_orphans_present(self):
        self.assertTrue(audit({"orphaned_row_count": 5}))

    def test_ok(self):
        self.assertFalse(audit({"orphaned_row_count": 0, "foreign_key_constraint_enforced": True}))
