import unittest
from agent import audit


class PaymentWebhookReconciliationAuditTests(unittest.TestCase):
    def test_unverified_signature(self):
        self.assertEqual("critical", audit({"signature_verified": False})[0]["severity"])

    def test_reconciled_flow(self):
        flow = {"signature_verified": True, "event_id_deduplication": True,
                "ledger_reconciliation": True, "failed_event_age_hours": 1}
        self.assertEqual([], audit(flow))


if __name__ == "__main__":
    unittest.main()
