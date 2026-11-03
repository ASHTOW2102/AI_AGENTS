import unittest
from agent import audit


class APIVersionNegotiationAuditTests(unittest.TestCase):

    def test_no_explicit_version(self):
        self.assertTrue(audit({"version_specified_by_client": False}))

    def test_ok(self):
        self.assertFalse(audit({"version_specified_by_client": True, "default_version_changes_without_notice": False}))
