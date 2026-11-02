import unittest
from agent import audit


class SessionFixationAuditTests(unittest.TestCase):

    def test_no_rotation(self):
        self.assertTrue(audit({"session_id_rotated_on_login": False}))

    def test_ok(self):
        self.assertFalse(audit({"session_id_rotated_on_login": True, "privilege_change_possible": False}))
