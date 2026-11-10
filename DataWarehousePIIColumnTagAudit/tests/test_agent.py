import unittest
from agent import audit


class DataWarehousePIIColumnTagAuditTests(unittest.TestCase):

    def test_untagged(self):
        self.assertTrue(audit({"pii_columns": ["ssn"], "tagged_columns": []}))

    def test_ok(self):
        self.assertFalse(audit({"pii_columns": ["ssn"], "tagged_columns": ["ssn"], "masking_policy_applied": True}))
