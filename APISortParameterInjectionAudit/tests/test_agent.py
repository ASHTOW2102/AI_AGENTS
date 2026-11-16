import unittest
from agent import audit


class APISortParameterInjectionAuditTests(unittest.TestCase):

    def test_unvalidated_sort(self):
        self.assertTrue(audit({"sort_param_from_client": True, "sort_param_allowlisted": False}))

    def test_ok(self):
        self.assertFalse(audit({"sort_param_from_client": True, "sort_param_allowlisted": True, "sort_param_concatenated_into_sql": False}))
