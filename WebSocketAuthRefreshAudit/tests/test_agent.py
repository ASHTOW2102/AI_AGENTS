import unittest
from agent import audit


class WebSocketAuthRefreshAuditTests(unittest.TestCase):
    def test_expiring_auth_without_reauth(self):
        self.assertIn("cannot reauthenticate", audit({"auth_expires_during_connection": True})[0]["issue"])

    def test_managed_connection(self):
        connection = {"auth_expires_during_connection": True, "reauthentication_supported": True,
                      "reauthentication_deadline_enforced": True, "revocation_required": True,
                      "active_connections_closed_on_revocation": True,
                      "max_connection_age_hours": 1, "approved_max_connection_age_hours": 24}
        self.assertEqual([], audit(connection))


if __name__ == "__main__":
    unittest.main()
