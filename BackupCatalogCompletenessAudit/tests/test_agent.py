import unittest
from agent import audit


class BackupCatalogCompletenessAuditTests(unittest.TestCase):

    def test_untracked_store(self):
        self.assertTrue(audit({"data_stores": ["a", "b"], "backed_up_stores": ["a"]}))

    def test_ok(self):
        self.assertFalse(audit({"data_stores": ["a"], "backed_up_stores": ["a"], "backup_jobs_missing_schedule": 0}))
