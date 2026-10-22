import unittest
from agent import audit


class PackageProvenanceAuditTests(unittest.TestCase):
    def test_unapproved_source(self):
        self.assertEqual("critical", audit({"unapproved_source": True})[-1]["severity"])

    def test_verified_package(self):
        package = {"source_registry": "internal", "version_pinned": True, "checksum_verified": True}
        self.assertEqual([], audit(package))


if __name__ == "__main__":
    unittest.main()
