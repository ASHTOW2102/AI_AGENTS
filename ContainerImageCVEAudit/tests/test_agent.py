import unittest
from agent import audit


class ContainerImageCVEAuditTests(unittest.TestCase):

    def test_critical_cve(self):
        self.assertTrue(audit({"critical_cve_count": 1, "critical_cve_waiver": False}))

    def test_ok(self):
        self.assertFalse(audit({"critical_cve_count": 0, "high_cve_count": 0, "scan_age_days": 1}))
