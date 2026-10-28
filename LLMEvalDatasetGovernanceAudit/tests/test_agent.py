import unittest
from agent import audit


class LLMEvalDatasetGovernanceAuditTests(unittest.TestCase):
    def test_unevaluated_overlap(self):
        self.assertIn("overlap risk", audit({"train_eval_overlap_possible": True})[0]["issue"])

    def test_governed_dataset(self):
        dataset = {"source_documented": True, "contains_personal_data": False,
                   "train_eval_overlap_possible": False, "versioned": True}
        self.assertEqual([], audit(dataset))


if __name__ == "__main__":
    unittest.main()
