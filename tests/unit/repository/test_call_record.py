from unittest import TestCase
from unittest.mock import patch, Mock
from pymongo.errors import DuplicateKeyError
from app import errors
from app.repository import schema
from app.repository.call_record import CallRecord
from app.repository.types import Document
from app.models.enums import CallRecordType


class TestCallRecord(TestCase):
    def setUp(self):
        self.mock_collection = Mock()
        CallRecord._instance = None
        self.repository = CallRecord(self.mock_collection)

    @patch.object(Document, "__init__", return_value=None)
    @patch("app.repository.schema.parse")
    def test_add(self, mock_parser, mock_dock_init):
        with self.subTest("when invalid type"):
            with self.assertRaises(KeyError):
                self.repository.add({"type": "start"})

        types = [CallRecordType.start, CallRecordType.end]

        for type_ in types:
            record = {"type": type_}

            mock_parser.reset()
            mock_dock_init.reset()

            with self.subTest("when invalid schema"):
                mock_parser.side_effect = ValueError
                with self.assertRaises(ValueError):
                    self.repository.add(record)

            mock_parser.side_effect = None
            mock_parser.return_value = "parsed"

            with self.subTest("when has duplicate keys "):
                self.mock_collection.insert_one.side_effect = DuplicateKeyError(
                    Exception())

                with self.assertRaises(errors.UnprocessableDataError):
                    self.repository.add(record)

            self.mock_collection.insert_one.side_effect = None

            with self.subTest("when inserted with success"):
                actual = self.repository.add(record)

                mock_parser.assert_called_with(
                    record, schema.CALL_RECORD[type_])
                mock_dock_init.assert_called_with(
                    "parsed", schema.CALL_RECORD[type_])

                self.assertIsInstance(actual, Document)
