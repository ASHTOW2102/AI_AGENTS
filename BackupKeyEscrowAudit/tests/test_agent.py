import unittest
from agent import audit


class BackupKeyEscrowAuditTests(unittest.TestCase):

    def test_not_escrowed(self):
        self.assertTrue(audit({"escrowed": False}))

    def test_ok(self):
        self.assertFalse(audit({"escrowed": True, "escrow_holder_count": 2, "escrow_access_logged": True}))
