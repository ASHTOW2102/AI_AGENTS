import unittest
from agent import audit


class TokenStorageClientSideAuditTests(unittest.TestCase):

    def test_localstorage(self):
        self.assertTrue(audit({"token_storage_location": "localStorage"}))

    def test_ok(self):
        self.assertFalse(audit({"token_storage_location": "cookie", "cookie_httponly": True}))
