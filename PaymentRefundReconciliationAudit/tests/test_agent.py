import unittest
from agent import audit


class PaymentRefundReconciliationAuditTests(unittest.TestCase):
    def test_ledger_mismatch(self):
        self.assertEqual("critical", audit({"provider_refunded_amount": 10, "ledger_refunded_amount": 8})[0]["severity"])

    def test_reconciled_refund(self):
        refund = {"refund_requested": True, "provider_status_confirmed": True,
                  "provider_refunded_amount": 10, "ledger_refunded_amount": 10,
                  "partial_refund_supported": False, "duplicate_refund_events": 0}
        self.assertEqual([], audit(refund))


if __name__ == "__main__":
    unittest.main()
