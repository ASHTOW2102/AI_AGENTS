import unittest
from agent import audit


class MobileAppUniversalLinkValidationAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"validates_universal_link_team_id": False}))

    def test_ok(self):
        self.assertFalse(audit({"validates_universal_link_team_id": True}))
