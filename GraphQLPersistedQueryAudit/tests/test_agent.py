import unittest
from agent import audit


class GraphQLPersistedQueryAuditTests(unittest.TestCase):

    def test_arbitrary_allowed(self):
        self.assertTrue(audit({"production": True, "allows_arbitrary_queries": True}))

    def test_ok(self):
        self.assertFalse(audit({"production": True, "allows_arbitrary_queries": False, "introspection_enabled": False}))
