from unittest import TestCase
from app.infrastructure.configuration import set_test_mode


class BaseSuite(TestCase):
    @classmethod
    def setUpClass(cls):
        set_test_mode()
        if cls is BaseSuite:
            raise unittest.SkipTest("Skip BaseTest tests, it's a base class")
        super(BaseSuite, cls).setUpClass()
