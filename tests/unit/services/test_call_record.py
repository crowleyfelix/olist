from unittest import TestCase
from unittest.mock import patch
from app.services.call_record import CallRecord


class TestCallRecord(TestCase):

    @patch("app.repository.build_call_record")
    def setUp(self, mock_builder):
        self.mock_repository = mock_builder()
        CallRecord._instance = None
        self.service = CallRecord()

    def test_create(self):
        self.mock_repository.add.return_value = "added"
        actual = self.service.create("record")
        self.assertEqual(actual, "added")
