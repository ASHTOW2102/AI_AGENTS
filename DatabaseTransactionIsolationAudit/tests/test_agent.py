import unittest
from agent import audit


class DatabaseTransactionIsolationAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"requires_serializable": True, "isolation_level": "READ_COMMITTED"}))

    def test_ok(self):
        self.assertFalse(audit({"requires_serializable": True, "isolation_level": "SERIALIZABLE"}))
