import unittest
from agent import audit


class RobotsIndexabilityAuditTests(unittest.TestCase):
    def test_production_blocked(self):
        self.assertEqual(2, len(audit({"production": True, "sitewide_noindex": True, "robots_disallow_all": True})))

    def test_indexable_site(self):
        site = {"production": True, "sitewide_noindex": False, "robots_disallow_all": False,
                "sitemap_url": "/sitemap.xml", "sitemap_fetchable": True, "canonical_mismatch_count": 0}
        self.assertEqual([], audit(site))


if __name__ == "__main__":
    unittest.main()
