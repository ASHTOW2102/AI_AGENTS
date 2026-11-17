import unittest
from agent import audit


class ServerlessLayerVersionPinningAuditTests(unittest.TestCase):

    def test_alias(self):
        self.assertTrue(audit({"layer_reference_type": "alias"}))

    def test_ok(self):
        self.assertFalse(audit({"layer_reference_type": "pinned_version"}))
