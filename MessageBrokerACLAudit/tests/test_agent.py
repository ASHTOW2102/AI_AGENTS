import unittest
from agent import audit


class MessageBrokerACLAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"default_acl_allow_all": True}))

    def test_ok(self):
        self.assertFalse(audit({"default_acl_allow_all": False}))
