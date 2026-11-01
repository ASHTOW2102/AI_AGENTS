import unittest
from agent import audit


class NetworkSegmentationAuditTests(unittest.TestCase):

    def test_public_to_data(self):
        self.assertTrue(audit({"source_zone": "public", "destination_zone": "data", "approved": False}))

    def test_ok(self):
        self.assertFalse(audit({"source_zone": "app", "destination_zone": "app"}))
