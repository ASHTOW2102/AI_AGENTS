import unittest
from agent import audit


class APIRequestSmugglingAuditTests(unittest.TestCase):

    def test_parser_mismatch(self):
        self.assertTrue(audit({"supports_chunked_encoding": True, "front_end_and_back_end_parsers_differ": True}))

    def test_ok(self):
        self.assertFalse(audit({"supports_chunked_encoding": True, "front_end_and_back_end_parsers_differ": False, "strict_content_length_validation": True}))
