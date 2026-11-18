import unittest
from agent import audit


class TokenRefreshRaceConditionAuditTests(unittest.TestCase):

    def test_race(self):
        self.assertTrue(audit({"concurrent_requests_possible": True, "refresh_request_deduplicated": False}))

    def test_ok(self):
        self.assertFalse(audit({"concurrent_requests_possible": True, "refresh_request_deduplicated": True, "refresh_mutex_or_lock_used": True}))
