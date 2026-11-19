import unittest
from agent import audit


class ContainerInitContainerFailureAuditTests(unittest.TestCase):

    def test_silent_failure(self):
        self.assertTrue(audit({"has_init_containers": True, "init_container_failure_blocks_main_container": False}))

    def test_ok(self):
        self.assertFalse(audit({"has_init_containers": True, "init_container_failure_blocks_main_container": True, "init_container_failures_alerted": True}))
