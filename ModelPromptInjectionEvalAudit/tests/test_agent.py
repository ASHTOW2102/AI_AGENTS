import unittest
from agent import audit


class ModelPromptInjectionEvalAuditTests(unittest.TestCase):
    def test_unsafe_tool_call(self):
        self.assertEqual("critical", audit({"unsafe_tool_calls": 1})[0]["severity"])

    def test_healthy_eval(self):
        run = {"attack_cases": 100, "minimum_attack_cases": 50, "blocked_attack_rate_percent": 99,
               "minimum_blocked_attack_rate_percent": 95, "unsafe_tool_calls": 0,
               "days_since_last_eval": 2, "max_eval_age_days": 30}
        self.assertEqual([], audit(run))


if __name__ == "__main__":
    unittest.main()
