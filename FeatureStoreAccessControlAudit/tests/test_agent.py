import unittest
from agent import audit


class FeatureStoreAccessControlAuditTests(unittest.TestCase):

    def test_unapproved_consumer(self):
        self.assertTrue(audit({"consumers": ["a", "b"], "approved_consumers": ["a"]}))

    def test_ok(self):
        self.assertFalse(audit({"consumers": ["a"], "approved_consumers": ["a"], "sensitive": False}))
