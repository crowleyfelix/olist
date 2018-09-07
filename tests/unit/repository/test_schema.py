from unittest import TestCase
from unittest.mock import patch
from app.repository import schema


class TestSchema(TestCase):
    def test_parse(self):
