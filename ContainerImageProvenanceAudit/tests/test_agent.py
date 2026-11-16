import unittest
from agent import audit


class ContainerImageProvenanceAuditTests(unittest.TestCase):

    def test_no_provenance(self):
        self.assertTrue(audit({"provenance_attestation_present": False}))

    def test_ok(self):
        self.assertFalse(audit({"provenance_attestation_present": True, "builder_identity_verified": True}))
