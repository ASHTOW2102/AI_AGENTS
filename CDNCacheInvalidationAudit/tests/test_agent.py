import unittest
from agent import audit


class CDNCacheInvalidationAuditTests(unittest.TestCase):

    def test_no_invalidation(self):
        self.assertTrue(audit({"content_changed": True, "invalidation_triggered": False}))

    def test_ok(self):
        self.assertFalse(audit({"content_changed": True, "invalidation_triggered": True, "invalidation_propagation_ms": 1000, "max_acceptable_propagation_ms": 60000, "stale_while_revalidate_configured": True}))
