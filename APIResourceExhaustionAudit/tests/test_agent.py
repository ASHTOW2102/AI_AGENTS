import unittest
from agent import audit


class APIResourceExhaustionAuditTests(unittest.TestCase):

    def test_unbounded_array(self):
        self.assertTrue(audit({"accepts_array_input": True, "max_array_length_enforced": False}))

    def test_ok(self):
        self.assertFalse(audit({"accepts_array_input": True, "max_array_length_enforced": True, "accepts_nested_json": True, "max_nesting_depth_enforced": True}))
