import unittest
from agent import audit


class LocalizationCoverageAuditTests(unittest.TestCase):
    def test_untranslated_strings(self):
        self.assertIn("2 required strings", audit({"required_strings": 10, "translated_strings": 8})[0]["issue"])

    def test_complete_locale(self):
        locale = {"required_strings": 10, "translated_strings": 10, "fallback_rate_percent": 1,
                  "max_fallback_rate_percent": 5, "missing_critical_strings": 0,
                  "stale_translation_days": 60, "max_translation_age_days": 365}
        self.assertEqual([], audit(locale))


if __name__ == "__main__":
    unittest.main()
