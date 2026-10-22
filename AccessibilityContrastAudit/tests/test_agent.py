import unittest
from agent import audit


class AccessibilityContrastAuditTests(unittest.TestCase):
    def test_low_contrast(self):
        self.assertIn("below", audit({"color_pairs": [{"element": "button", "contrast_ratio": 2, "required_ratio": 4.5}]})[0]["issue"])

    def test_passing_scan(self):
        self.assertEqual([], audit({"color_pairs": [{"contrast_ratio": 5, "required_ratio": 4.5}], "unlabeled_controls": 0}))


if __name__ == "__main__":
    unittest.main()
