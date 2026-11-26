import unittest
from agent import audit


class GitBranchProtectionAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"is_default_branch": True, "allows_force_push": True, "requires_pr_review": True}))

    def test_ok(self):
        self.assertFalse(audit({"is_default_branch": True, "allows_force_push": False, "requires_pr_review": True}))
