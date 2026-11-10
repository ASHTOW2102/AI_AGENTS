import unittest
from agent import audit


class TokenAudienceMismatchAuditTests(unittest.TestCase):

    def test_mismatch(self):
        self.assertTrue(audit({"audience_claim": "svc-a", "expected_service_id": "svc-b"}))

    def test_ok(self):
        self.assertFalse(audit({"audience_claim": "svc-a", "expected_service_id": "svc-a", "audience_validated": True}))
