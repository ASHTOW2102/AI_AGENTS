import unittest
from agent import audit


class DNSSECConfigAuditTests(unittest.TestCase):
    def test_unsigned_zone(self):
        self.assertEqual("high", audit({"dnssec_enabled": False})[0]["severity"])

    def test_safe_zone(self):
        self.assertEqual([], audit({"dnssec_enabled": True, "ds_published": True, "key_age_days": 30,
                                    "max_key_age_days": 365}))


if __name__ == "__main__":
    unittest.main()
