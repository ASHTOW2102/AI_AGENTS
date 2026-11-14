import unittest
from agent import audit


class WebAppClickjackingAuditTests(unittest.TestCase):

    def test_no_protection(self):
        self.assertTrue(audit({"x_frame_options": None, "csp_directives": []}))

    def test_ok(self):
        self.assertFalse(audit({"x_frame_options": "DENY", "csp_directives": ["frame-ancestors"]}))
