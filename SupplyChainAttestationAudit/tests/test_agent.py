import unittest
from agent import audit


class SupplyChainAttestationAuditTests(unittest.TestCase):
    def test_missing_attestation(self):
        self.assertIn("no supply-chain attestation", audit({})[0]["issue"])

    def test_trusted_artifact(self):
        artifact = {"attestation_present": True, "signature_verified": True, "source_revision": "abc123",
                    "builder_identity": "ci-prod", "approved_builders": ["ci-prod"]}
        self.assertEqual([], audit(artifact))


if __name__ == "__main__":
    unittest.main()
