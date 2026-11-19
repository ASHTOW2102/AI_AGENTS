import unittest
from agent import audit


class DataLineageProvenanceGapAuditTests(unittest.TestCase):

    def test_no_lineage(self):
        self.assertTrue(audit({"is_derived": True, "lineage_recorded": False}))

    def test_ok(self):
        self.assertFalse(audit({"is_derived": True, "lineage_recorded": True, "lineage_includes_transformation_logic": True}))
