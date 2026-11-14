import unittest
from agent import audit


class SearchQueryPIIRedactionAuditTests(unittest.TestCase):

    def test_unredacted(self):
        self.assertTrue(audit({"logs_raw_queries": True, "pii_redaction_applied": False}))

    def test_ok(self):
        self.assertFalse(audit({"logs_raw_queries": True, "pii_redaction_applied": True, "redaction_coverage_tested": True}))
