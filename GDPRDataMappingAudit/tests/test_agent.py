import unittest
from agent import audit


class GDPRDataMappingAuditTests(unittest.TestCase):

    def test_no_legal_basis(self):
        self.assertTrue(audit({"legal_basis": None}))

    def test_ok(self):
        self.assertFalse(audit({"legal_basis": "consent", "purpose": "x"}))
