import unittest
from agent import audit


class DatabaseReadAfterWriteConsistencyAuditTests(unittest.TestCase):

    def test_no_guarantee(self):
        self.assertTrue(audit({"reads_from_replica_after_write": True, "read_after_write_guarantee_mechanism": None}))

    def test_ok(self):
        self.assertFalse(audit({"reads_from_replica_after_write": True, "read_after_write_guarantee_mechanism": "session_pinning"}))
