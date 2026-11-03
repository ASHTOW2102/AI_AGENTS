import unittest
from agent import audit


class KubernetesPodAntiAffinityAuditTests(unittest.TestCase):

    def test_no_anti_affinity(self):
        self.assertTrue(audit({"critical": True, "anti_affinity_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"critical": True, "anti_affinity_configured": True, "topology_spread_zone_aware": True}))
