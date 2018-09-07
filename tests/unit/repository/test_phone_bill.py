from datetime import datetime
from unittest import TestCase
from unittest.mock import patch, Mock
from pymongo.errors import DuplicateKeyError
from app import errors
from app.repository import schema, query
from app.repository.phone_bill import PhoneBill
from app.repository.types import Documents


class TestPhoneBill(TestCase):
    def setUp(self):
        self.mock_collection = Mock()
        PhoneBill._instance = None
        self.repository = PhoneBill(self.mock_collection)

    @patch.object(Documents, "__init__", return_value=None)
    @patch("app.repository.schema.parse")
    def test_add(self, mock_parser, mock_doc_init):
        bill = "bill"

        with self.subTest("when invalid schema"):
            mock_parser.side_effect = ValueError
            with self.assertRaises(ValueError):
                self.repository.add(bill)

        mock_parser.side_effect = None
        mock_parser.return_value = "parsed"

        with self.subTest("when has duplicate keys "):
            self.mock_collection.insert_many.side_effect = DuplicateKeyError(
                Exception())

            with self.assertRaises(errors.UnprocessableDataError):
                self.repository.add(bill)

        self.mock_collection.insert_many.side_effect = None

        with self.subTest("when inserted with success"):
            actual = self.repository.add(bill)

            mock_parser.assert_called_with(
                bill, [schema.PHONE_BILL])

            self.assertIsInstance(actual, Documents)

    @patch.object(Documents, "__init__", return_value=None)
    @patch("app.processors.paging.process", return_value="page")
    @patch("app.repository.query.build", return_value="builded")
    def test_search(self, mock_query_builder, mock_page_processor, mock_doc_init):
        phone_number = "123456789"
        period = "2016-02"
        page = 1
        limit = 10

        self.mock_collection.find.return_value = "data"
        self.mock_collection.count.return_value = 100

        self.repository.search(phone_number, period, page, limit)

        mock_query_builder.assert_called_once_with(query.FIND_PHONE_BILL,
                                                   phone_number=phone_number,
                                                   period=period)
        self.mock_collection.find.assert_called_once_with("builded")
        mock_page_processor.assert_called_once_with(1, 10, 100)
        mock_doc_init.assert_called_once_with(
            "data", schema.PHONE_BILL, page, limit)
