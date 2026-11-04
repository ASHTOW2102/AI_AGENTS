import unittest
from agent import audit


class ContainerSBOMAttachmentAuditTests(unittest.TestCase):

    def test_no_sbom(self):
        self.assertTrue(audit({"sbom_attached": False}))

    def test_ok(self):
        self.assertFalse(audit({"sbom_attached": True, "sbom_signature_verified": True, "sbom_age_days": 1, "image_age_days": 1}))
