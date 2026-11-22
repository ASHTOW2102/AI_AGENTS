import unittest
from agent import audit


class BackgroundJobIdempotencyAuditTests(unittest.TestCase):

    def test_side_effects_no_idempotency_key(self):
        self.assertTrue(audit({"performs_external_side_effects": True, "uses_idempotency_key": False}))

    def test_ok(self):
        self.assertFalse(audit({"performs_external_side_effects": True, "uses_idempotency_key": True, "at_least_once_delivery": True, "is_handler_idempotent": True}))
