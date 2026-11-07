import unittest
from agent import audit


class APISchemaVersionSkewAuditTests(unittest.TestCase):

    def test_version_skew(self):
        self.assertTrue(audit({"producer_schema_version": "v2", "consumer_schema_version": "v1"}))

    def test_ok(self):
        self.assertFalse(audit({"producer_schema_version": "v2", "consumer_schema_version": "v2", "schema_registry_checked": True, "breaking_change_detected": False}))
