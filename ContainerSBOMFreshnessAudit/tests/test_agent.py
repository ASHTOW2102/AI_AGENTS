import unittest
from agent import audit


class ContainerSBOMFreshnessAuditTests(unittest.TestCase):

    def test_missing_sbom(self):
        self.assertTrue(audit({"sbom_present": False}))

    def test_ok(self):
        self.assertFalse(audit({"sbom_present": True, "sbom_age_days": 1, "image_age_days": 5}))
