import unittest
from agent import audit


class APIHTTPPipeliningDesyncAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"frontend_parses_chunked_strictly": True, "backend_parses_chunked_strictly": False}))

    def test_ok(self):
        self.assertFalse(audit({"frontend_parses_chunked_strictly": True, "backend_parses_chunked_strictly": True}))
