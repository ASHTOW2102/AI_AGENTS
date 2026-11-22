import unittest
from agent import audit


class GraphQLDepthLimitAuditTests(unittest.TestCase):

    def test_no_max_depth(self):
        self.assertTrue(audit({"max_query_depth": None}))

    def test_ok(self):
        self.assertFalse(audit({"max_query_depth": 8, "allows_recursive_fragments": False}))
