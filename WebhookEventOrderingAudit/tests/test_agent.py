import unittest
from agent import audit


class WebhookEventOrderingAuditTests(unittest.TestCase):

    def test_no_sequence(self):
        self.assertTrue(audit({"ordering_matters": True, "sequence_number_included": False}))

    def test_ok(self):
        self.assertFalse(audit({"ordering_matters": True, "sequence_number_included": True, "consumer_reorders_on_receipt": True, "retries_can_reorder_delivery": False}))
