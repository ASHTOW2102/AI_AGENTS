import unittest
from agent import audit


class APIPaginationLimitAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"enforces_max_page_size": False}))

    def test_ok(self):
        self.assertFalse(audit({"enforces_max_page_size": True, "max_page_size": 100}))
