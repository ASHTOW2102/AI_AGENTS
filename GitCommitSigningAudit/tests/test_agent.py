import unittest
from agent import audit


class GitCommitSigningAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"requires_signed_commits": False}))

    def test_ok(self):
        self.assertFalse(audit({"requires_signed_commits": True}))
