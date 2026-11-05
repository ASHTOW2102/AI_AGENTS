import unittest
from agent import audit


class DatabaseForeignKeyIntegrityAuditTests(unittest.TestCase):

    def test_unenforced_fk(self):
        self.assertTrue(audit({"logical_fk_count": 1, "fk_constraint_enforced": False}))

    def test_ok(self):
        self.assertFalse(audit({"logical_fk_count": 1, "fk_constraint_enforced": True, "orphaned_row_count": 0}))
