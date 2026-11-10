import unittest
from agent import audit


class APIIdempotencyKeyReuseAuditTests(unittest.TestCase):

    def test_key_body_mismatch(self):
        self.assertTrue(audit({"idempotency_key_reused": True, "body_hash": "a", "original_body_hash": "b"}))

    def test_ok(self):
        self.assertFalse(audit({"idempotency_key_reused": False, "mutating_method": True, "idempotency_key_present": True}))
