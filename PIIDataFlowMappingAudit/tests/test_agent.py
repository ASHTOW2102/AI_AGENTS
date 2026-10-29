import unittest
from agent import audit


class PIIDataFlowMappingAuditTests(unittest.TestCase):
    def test_missing_destination(self):
        self.assertIn("no documented destinations", audit({"contains_personal_data": True})[0]["issue"])

    def test_mapped_flow(self):
        flow = {"contains_personal_data": True, "purpose_documented": True,
                "destinations": ["service-a"], "required_controls": ["encryption"],
                "implemented_controls": ["encryption"], "last_review_date": "2026-10-01"}
        self.assertEqual([], audit(flow))


if __name__ == "__main__":
    unittest.main()
