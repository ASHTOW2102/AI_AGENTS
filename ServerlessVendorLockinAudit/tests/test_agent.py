import unittest
from agent import audit


class ServerlessVendorLockinAuditTests(unittest.TestCase):

    def test_tight_coupling(self):
        self.assertTrue(audit({"proprietary_event_format_count": 3, "adapter_layer_present": False}))

    def test_ok(self):
        self.assertFalse(audit({"proprietary_event_format_count": 0, "uses_proprietary_managed_database": False}))
