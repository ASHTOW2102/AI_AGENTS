import unittest
from agent import audit


class APIClientSDKVersionAuditTests(unittest.TestCase):

    def test_deprecated(self):
        self.assertTrue(audit({"sdk_version": "1.0", "deprecated_versions": ["1.0"]}))

    def test_ok(self):
        self.assertFalse(audit({"sdk_version": "2.0", "deprecated_versions": ["1.0"], "sdk_age_days": 30}))
