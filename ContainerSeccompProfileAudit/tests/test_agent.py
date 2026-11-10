import unittest
from agent import audit


class ContainerSeccompProfileAuditTests(unittest.TestCase):

    def test_unconfined(self):
        self.assertTrue(audit({"seccomp_profile": "unconfined"}))

    def test_ok(self):
        self.assertFalse(audit({"seccomp_profile": "runtime/default"}))
