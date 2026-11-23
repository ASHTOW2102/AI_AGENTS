import unittest
from agent import audit


class GraphQLIntrospectionExposureAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"introspection_enabled": True, "environment": "production"}))

    def test_ok(self):
        self.assertFalse(audit({"introspection_enabled": True, "environment": "development"}))
