import unittest
from agent import audit


class ServiceMeshHeaderPropagationAuditTests(unittest.TestCase):

    def test_no_propagation(self):
        self.assertTrue(audit({"makes_downstream_calls": True, "propagates_trace_headers": False}))

    def test_ok(self):
        self.assertFalse(audit({"makes_downstream_calls": True, "propagates_trace_headers": True, "propagation_tested": True}))
