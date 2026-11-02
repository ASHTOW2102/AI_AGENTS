import unittest
from agent import audit


class APIRequestIDPropagationAuditTests(unittest.TestCase):

    def test_no_propagation(self):
        self.assertTrue(audit({"calls_downstream": True, "propagates_request_id_downstream": False}))

    def test_ok(self):
        self.assertFalse(audit({"accepts_incoming_request_id": True, "calls_downstream": False, "request_id_in_logs": True}))
