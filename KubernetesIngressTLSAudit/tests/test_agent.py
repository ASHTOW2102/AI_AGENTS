import unittest
from agent import audit


class KubernetesIngressTLSAuditTests(unittest.TestCase):
    def test_public_plaintext_ingress(self):
        self.assertIn("no TLS", audit({"public": True})[0]["issue"])

    def test_secure_ingress(self):
        ingress = {"public": True, "tls_secret": "web-cert", "https_redirect": True,
                   "hosts": ["app.example.test"], "certificate_hosts": ["app.example.test"], "tls_min_version": "TLS1.2"}
        self.assertEqual([], audit(ingress))


if __name__ == "__main__":
    unittest.main()
