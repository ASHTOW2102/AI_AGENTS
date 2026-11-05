import unittest
from agent import audit


class DataPipelineLineageGapAuditTests(unittest.TestCase):

    def test_untracked_output(self):
        self.assertTrue(audit({"output_datasets": ["a"], "lineage_tracked_datasets": []}))

    def test_ok(self):
        self.assertFalse(audit({"output_datasets": ["a"], "lineage_tracked_datasets": ["a"], "transforms_pii": False}))
