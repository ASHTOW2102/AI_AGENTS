import unittest
from agent import audit


class KubernetesCRDVersionSkewAuditTests(unittest.TestCase):

    def test_no_conversion(self):
        self.assertTrue(audit({"served_version_deprecated": True, "conversion_webhook_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"served_version_deprecated": True, "conversion_webhook_configured": True, "removal_date_announced": True}))
