import unittest
from agent import audit


class SecretsManagerVersionPruningAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"old_version_count": 50, "max_retained_versions": 5}))

    def test_ok(self):
        self.assertFalse(audit({"old_version_count": 3, "max_retained_versions": 5}))
