import unittest
from agent import audit


class CISecretExposureAuditTests(unittest.TestCase):
    def test_fork_secret_exposure(self):
        self.assertEqual("critical", audit({"secrets_available_to_untrusted_forks": True})[0]["severity"])

    def test_trusted_workflow(self):
        self.assertEqual([], audit({"secrets_available_to_untrusted_forks": False,
                                    "executes_checkout_code": False, "secrets_logged": False,
                                    "static_credentials": False}))


if __name__ == "__main__":
    unittest.main()
