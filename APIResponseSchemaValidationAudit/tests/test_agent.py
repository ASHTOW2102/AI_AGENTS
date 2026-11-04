import unittest
from agent import audit


class APIResponseSchemaValidationAuditTests(unittest.TestCase):

    def test_not_validated(self):
        self.assertTrue(audit({"response_schema_declared": True, "schema_validated_before_send": False}))

    def test_ok(self):
        self.assertFalse(audit({"response_schema_declared": True, "schema_validated_before_send": True, "schema_validation_failures_in_production": 0}))
