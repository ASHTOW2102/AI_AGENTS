import unittest
from agent import audit


class DatabaseSchemaMigrationLockAuditTests(unittest.TestCase):

    def test_large_table_lock(self):
        self.assertTrue(audit({"takes_exclusive_lock": True, "table_row_count": 5000000, "large_table_threshold": 1000000}))

    def test_ok(self):
        self.assertFalse(audit({"takes_exclusive_lock": False, "table_row_count": 5000000, "large_table_threshold": 1000000, "scheduled_during_business_hours": False}))
