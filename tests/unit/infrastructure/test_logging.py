import os
from unittest.mock import patch, Mock
from unittest import TestCase
from app.infrastructure import logging
from . import fixtures


class TestLogging(TestCase):

    @patch("app.infrastructure.logging.get_config", fixtures.config)
    @patch("logging.basicConfig")
    def test_setup(self, mock_setup_log):
        logging.setup()
        mock_setup_log.assert_called_once_with(**fixtures.config().logging)
