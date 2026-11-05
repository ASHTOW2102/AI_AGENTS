import unittest
from agent import audit


class APIHATEOASLinkAuditTests(unittest.TestCase):

    def test_missing_href(self):
        self.assertTrue(audit({"links": [{"rel": "next", "href": None}]}))

    def test_ok(self):
        self.assertFalse(audit({"links": [{"rel": "next", "href": "x"}], "state": "active"}))
