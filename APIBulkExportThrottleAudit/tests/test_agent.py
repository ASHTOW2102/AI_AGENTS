import unittest
from agent import audit


class APIBulkExportThrottleAuditTests(unittest.TestCase):

    def test_no_cap(self):
        self.assertTrue(audit({"max_rows_per_export": None}))

    def test_ok(self):
        self.assertFalse(audit({"max_rows_per_export": 5000, "recommended_row_cap": 10000}))
