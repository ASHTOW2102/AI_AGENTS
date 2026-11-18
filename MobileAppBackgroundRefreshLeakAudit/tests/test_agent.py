import unittest
from agent import audit


class MobileAppBackgroundRefreshLeakAuditTests(unittest.TestCase):

    def test_not_cancelled(self):
        self.assertTrue(audit({"has_background_refresh": True, "background_refresh_cancelled_on_logout": False}))

    def test_ok(self):
        self.assertFalse(audit({"has_background_refresh": True, "background_refresh_cancelled_on_logout": True, "background_fetch_requires_valid_session": True}))
