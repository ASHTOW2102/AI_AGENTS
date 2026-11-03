import unittest
from agent import audit


class ContainerBaseImageFreshnessAuditTests(unittest.TestCase):

    def test_stale_base(self):
        self.assertTrue(audit({"base_image_age_days": 200, "max_base_image_age_days": 90}))

    def test_ok(self):
        self.assertFalse(audit({"base_image_age_days": 10, "base_image_pinned_by_digest": True}))
