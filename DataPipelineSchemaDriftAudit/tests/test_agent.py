import unittest
from agent import audit


class DataPipelineSchemaDriftAuditTests(unittest.TestCase):

    def test_unvalidated_drift(self):
        self.assertTrue(audit({"upstream_schema_changed": True, "schema_validation_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"upstream_schema_changed": False, "schema_validation_enabled": True, "schema_change_alerting": True}))
