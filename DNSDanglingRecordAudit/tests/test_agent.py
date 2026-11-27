import unittest
from agent import audit


class DNSDanglingRecordAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"points_to_deprovisioned_resource": True}))

    def test_ok(self):
        self.assertFalse(audit({"points_to_deprovisioned_resource": False}))
