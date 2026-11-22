import unittest
from agent import audit


class DataPipelineSchemaDriftAuditTests(unittest.TestCase):

    def test_no_validation(self):
        self.assertTrue(audit({"validates_input_schema": False}))

    def test_ok(self):
        self.assertFalse(audit({"validates_input_schema": True, "fails_closed_on_schema_mismatch": True}))
