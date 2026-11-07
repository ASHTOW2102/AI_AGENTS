import unittest
from agent import audit


class KubernetesPodDisruptionBudgetAuditTests(unittest.TestCase):

    def test_missing_pdb(self):
        self.assertTrue(audit({"replica_count": 3, "pdb_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"replica_count": 3, "pdb_configured": True, "min_available": 1}))
