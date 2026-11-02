import unittest
from agent import audit


class KubernetesTaintTolerationAuditTests(unittest.TestCase):

    def test_tolerates_all(self):
        self.assertTrue(audit({"tolerates_all_taints": True}))

    def test_ok(self):
        self.assertFalse(audit({"tolerates_all_taints": False, "tolerations": [{"operator": "Equal", "key": "dedicated"}]}))
