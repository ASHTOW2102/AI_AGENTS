import unittest
from agent import audit


class WebAppCSPReportOnlyAuditTests(unittest.TestCase):

    def test_stuck_report_only(self):
        self.assertTrue(audit({"csp_report_only": True, "report_only_days": 90, "max_acceptable_report_only_days": 30}))

    def test_ok(self):
        self.assertFalse(audit({"csp_report_only": False, "csp_enforced": True}))
