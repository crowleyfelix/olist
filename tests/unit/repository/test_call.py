from datetime import datetime
from unittest import TestCase
from unittest.mock import patch, Mock
from pymongo.errors import DuplicateKeyError
from app.repository import schema, query
from app.repository.call import Call
from app.repository.types import Documents


class TestCall(TestCase):
    def setUp(self):
        self.mock_collection = Mock()
        Call._instance = None
        self.repository = Call(self.mock_collection)

    @patch.object(Documents, "__init__", return_value=None)
    @patch("app.repository.query.build", return_value="builded")
    def test_search(self, mock_query_builder, mock_dock_init):
        phone_number = "123456789"
        start_date = datetime.now()
        end_date = datetime.now()
        self.mock_collection.aggregate.return_value = "data"

        self.repository.search(phone_number, start_date, end_date)

        mock_query_builder.assert_called_once_with(query.LIST_CALLS,
                                                   source=phone_number,
                                                   start_timestamp=start_date.timestamp(),
                                                   end_timestamp=end_date.timestamp())
        self.mock_collection.aggregate.assert_called_once_with("builded")
        mock_dock_init.assert_called_once_with("data", schema.CALL)
