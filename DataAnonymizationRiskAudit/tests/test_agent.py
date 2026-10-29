import unittest
from agent import audit


class DataAnonymizationRiskAuditTests(unittest.TestCase):
    def test_direct_identifiers(self):
        self.assertEqual("critical", audit({"direct_identifiers_present": True})[0]["severity"])

    def test_assessed_dataset(self):
        dataset = {"direct_identifiers_present": False, "quasi_identifiers_count": 0,
                   "pseudonymized": False, "reidentification_tested": True}
        self.assertEqual([], audit(dataset))


if __name__ == "__main__":
    unittest.main()
