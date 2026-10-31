import unittest
from agent import audit


class APIKeyExposureScanAuditTests(unittest.TestCase):
    def test_active_key_findings(self):
        self.assertEqual("critical", audit({"active_secret_findings": 1})[0]["severity"])

    def test_clean_scan(self):
        scan = {"active_secret_findings": 0, "scan_completed": True,
                "history_scan_enabled": True, "exceptions_unreviewed": 0}
        self.assertEqual([], audit(scan))


if __name__ == "__main__":
    unittest.main()
