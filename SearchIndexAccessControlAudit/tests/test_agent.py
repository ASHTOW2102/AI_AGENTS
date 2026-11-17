import unittest
from agent import audit


class SearchIndexAccessControlAuditTests(unittest.TestCase):

    def test_no_filter(self):
        self.assertTrue(audit({"multi_tenant_documents": True, "document_level_access_filter_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"multi_tenant_documents": True, "document_level_access_filter_enabled": True, "filter_bypass_tested": True}))
