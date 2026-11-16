import unittest
from agent import audit


class DatabaseVacuumSchedulingAuditTests(unittest.TestCase):

    def test_disabled(self):
        self.assertTrue(audit({"autovacuum_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"autovacuum_enabled": True, "dead_tuple_ratio": 0.05, "max_acceptable_dead_tuple_ratio": 0.2}))
