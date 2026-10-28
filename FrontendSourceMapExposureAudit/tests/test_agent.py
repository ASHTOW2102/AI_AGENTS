import unittest
from agent import audit


class FrontendSourceMapExposureAuditTests(unittest.TestCase):
    def test_unapproved_public_maps(self):
        self.assertIn("publicly published", audit({"production": True, "public_source_maps": True})[0]["issue"])

    def test_private_upload_only(self):
        build = {"production": True, "public_source_maps": False,
                 "source_maps_required_for_monitoring": True, "upload_to_private_monitoring": True}
        self.assertEqual([], audit(build))


if __name__ == "__main__":
    unittest.main()
