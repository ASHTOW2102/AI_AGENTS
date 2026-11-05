import unittest
from agent import audit


class TokenBindingAuditTests(unittest.TestCase):

    def test_unbound_privileged(self):
        self.assertTrue(audit({"highly_privileged": True, "bound_to_client_or_device": False}))

    def test_ok(self):
        self.assertFalse(audit({"highly_privileged": True, "bound_to_client_or_device": True, "binding_verified_on_each_use": True, "transmitted_via_url_query_param": False}))
