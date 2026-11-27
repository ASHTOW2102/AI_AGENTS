import unittest
from agent import audit


class APIErrorMessageLeakageAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"exposes_stack_traces_in_errors": True}))

    def test_ok(self):
        self.assertFalse(audit({"exposes_stack_traces_in_errors": False}))
