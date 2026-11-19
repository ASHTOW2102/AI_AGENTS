import unittest
from agent import audit


class APIQueryParamInjectionAuditTests(unittest.TestCase):

    def test_unescaped_shell(self):
        self.assertTrue(audit({"query_param_passed_to_shell": True, "shell_arg_escaping_applied": False}))

    def test_ok(self):
        self.assertFalse(audit({"query_param_passed_to_shell": False, "query_param_used_as_file_path": True, "path_traversal_sanitized": True}))
