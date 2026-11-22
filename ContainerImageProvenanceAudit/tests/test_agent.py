import unittest
from agent import audit


class ContainerImageProvenanceAuditTests(unittest.TestCase):

    def test_no_verification(self):
        self.assertTrue(audit({"verifies_image_signature": False}))

    def test_ok(self):
        self.assertFalse(audit({"verifies_image_signature": True, "enforces_at_admission": True, "enforces_signature_at_admission": True}))
