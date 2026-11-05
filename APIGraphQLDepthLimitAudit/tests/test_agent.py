import unittest
from agent import audit


class APIGraphQLDepthLimitAuditTests(unittest.TestCase):

    def test_no_depth_limit(self):
        self.assertTrue(audit({"max_query_depth_enforced": False}))

    def test_ok(self):
        self.assertFalse(audit({"max_query_depth_enforced": True, "max_field_count_enforced": True, "has_circular_relationships": False}))
