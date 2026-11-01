import unittest
from agent import audit


class GitSecretHistoryAuditTests(unittest.TestCase):

    def test_leak_not_rotated(self):
        self.assertTrue(audit({"secrets_found": 1, "secrets_rotated": False}))

    def test_ok(self):
        self.assertFalse(audit({"secrets_found": 0, "scan_age_days": 1}))
