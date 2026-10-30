import unittest
from agent import audit


class BrowserPermissionsPolicyAuditTests(unittest.TestCase):
    def test_unapproved_feature(self):
        self.assertIn("geolocation", audit({"enabled_features": ["geolocation"], "approved_features": []})[0]["issue"])

    def test_restricted_policy(self):
        policy = {"enabled_features": ["camera"], "approved_features": ["camera"],
                  "feature_allowlists": {"camera": ["self"]}, "cross_origin_iframes": False}
        self.assertEqual([], audit(policy))


if __name__ == "__main__":
    unittest.main()
