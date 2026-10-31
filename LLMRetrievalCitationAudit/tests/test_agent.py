import unittest
from agent import audit


class LLMRetrievalCitationAuditTests(unittest.TestCase):
    def test_retrieval_without_citations(self):
        self.assertIn("cites no sources", audit({"retrieved_chunks": 4, "cited_chunks": 0})[0]["issue"])

    def test_citations_present(self):
        answer = {"retrieved_chunks": 4, "cited_chunks": 2, "source_ids_present": True,
                  "source_ids_validated": True, "citation_required": True, "citation_rendered": True}
        self.assertEqual([], audit(answer))


if __name__ == "__main__":
    unittest.main()
