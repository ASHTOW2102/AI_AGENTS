import unittest
from agent import audit


class MobileAppInterProcessCommunicationAuditTests(unittest.TestCase):

    def test_unprotected_export(self):
        self.assertTrue(audit({"exported_components": ["ShareActivity"], "components_with_permission_checks": []}))

    def test_ok(self):
        self.assertFalse(audit({"exported_components": ["ShareActivity"], "components_with_permission_checks": ["ShareActivity"], "ipc_input_validated": True}))
