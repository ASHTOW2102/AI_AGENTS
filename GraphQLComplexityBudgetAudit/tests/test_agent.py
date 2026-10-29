import unittest
from agent import audit


class GraphQLComplexityBudgetAuditTests(unittest.TestCase):
    def test_unbounded_complexity(self):
        self.assertIn("not bounded", audit({})[0]["issue"])

    def test_bounded_queries(self):
        schema = {"complexity_limit_enabled": True, "max_query_depth": 5,
                  "approved_max_depth": 10, "list_fields_without_pagination": 0,
                  "batching_enabled": True, "batch_size_limit": 20}
        self.assertEqual([], audit(schema))


if __name__ == "__main__":
    unittest.main()
