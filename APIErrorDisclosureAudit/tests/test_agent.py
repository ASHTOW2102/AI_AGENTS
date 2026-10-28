import unittest
from agent import audit


class APIErrorDisclosureAuditTests(unittest.TestCase):
    def test_personal_data_is_critical(self):
        self.assertEqual("critical", audit({"error_contains_personal_data": True})[-1]["severity"])

    def test_sanitized_error(self):
        response = {"production": True, "stack_trace_in_body": False,
                    "database_error_details_exposed": False, "request_id_enabled": True,
                    "request_id_in_error": True, "error_contains_personal_data": False}
        self.assertEqual([], audit(response))


if __name__ == "__main__":
    unittest.main()
