import unittest
from agent import audit


class ServerlessProvisionedConcurrencyWasteAuditTests(unittest.TestCase):

    def test_overprovisioned(self):
        self.assertTrue(audit({"provisioned_concurrency": 100, "peak_concurrent_invocations": 10, "max_acceptable_overprovision_ratio": 1.5}))

    def test_ok(self):
        self.assertFalse(audit({"provisioned_concurrency": 10, "peak_concurrent_invocations": 8, "max_acceptable_overprovision_ratio": 1.5, "usage_reviewed_recently": True}))
