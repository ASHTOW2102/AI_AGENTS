import unittest
from agent import audit


class APIErrorMessageInformationLeakAuditTests(unittest.TestCase):

    def test_stack_trace(self):
        self.assertTrue(audit({"returns_stack_trace_to_client": True}))

    def test_ok(self):
        self.assertFalse(audit({"returns_stack_trace_to_client": False, "error_message_includes_internal_paths": False}))
