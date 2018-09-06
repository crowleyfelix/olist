import os
from munch import Munch
from unittest.mock import patch, Mock
from unittest import TestCase
from app.infrastructure import configuration

MOCK_CONFIG = {}


class TestConfiguration(TestCase):
    def setUp(self):
        MOCK_CONFIG.clear()

    @patch.dict(os.environ, MOCK_CONFIG, True)
    def test_get_config(self):
        mandatory_config = [
            "MONGO_URI",
            "MONGO_DATABASE",
        ]

        for mandatory in mandatory_config:
            configuration._CONFIG.clear()

            with self.assertRaises(KeyError):
                configuration.get_config()

            os.environ.update({mandatory: "1"})

        configuration.get_config()
