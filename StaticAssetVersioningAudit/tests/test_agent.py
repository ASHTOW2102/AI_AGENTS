import unittest
from agent import audit


class StaticAssetVersioningAuditTests(unittest.TestCase):

    def test_long_cache_no_hash(self):
        self.assertTrue(audit({"cache_max_age_seconds": 31536000, "content_hash_in_filename": False}))

    def test_ok(self):
        self.assertFalse(audit({"cache_max_age_seconds": 31536000, "content_hash_in_filename": True, "immutable_directive_present": True}))
