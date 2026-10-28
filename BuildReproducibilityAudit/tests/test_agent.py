import unittest
from agent import audit


class BuildReproducibilityAuditTests(unittest.TestCase):
    def test_digest_mismatch(self):
        self.assertIn("digests do not match", audit({"reproducible_check_required": True,
                                                       "artifact_digest_matches": False})[0]["issue"])

    def test_reproducible_metadata(self):
        build = {"dependency_lockfile_used": True, "build_environment_pinned": True,
                 "reproducible_check_required": True, "artifact_digest_matches": True,
                 "source_revision_recorded": True}
        self.assertEqual([], audit(build))


if __name__ == "__main__":
    unittest.main()
