import unittest
from agent import audit


class ApiPaginationContractAuditTests(unittest.TestCase):
    def test_unbounded_page_size(self):
        self.assertIn("maximum page-size", audit({"pagination_supported": True})[0]["issue"])

    def test_bounded_cursor_contract(self):
        item = {"pagination_supported": True, "max_page_size": 100, "mutable_collection": True,
                "cursor_pagination": True, "has_next": False}
        self.assertEqual([], audit(item))


if __name__ == "__main__":
    unittest.main()
