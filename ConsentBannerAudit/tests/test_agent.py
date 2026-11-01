import unittest
from agent import audit


class ConsentBannerAuditTests(unittest.TestCase):

    def test_preset_cookies(self):
        self.assertTrue(audit({"non_essential_cookies_set_before_consent": True}))

    def test_ok(self):
        self.assertFalse(audit({"default_state": "all_rejected", "reject_all_option": True, "category_level_choice": True}))
