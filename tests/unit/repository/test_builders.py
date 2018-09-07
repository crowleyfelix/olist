from unittest import TestCase
from unittest.mock import patch
from app.repository import builders, constants
from app.repository.call_record import CallRecord
from app.repository.call import Call
from app.repository.phone_bill import PhoneBill


class TestBuilders(TestCase):
    def setUp(self):
        Call._instance = None
        CallRecord._instance = None
        PhoneBill._instance = None

    @patch("app.repository.mongo.get_collection", return_value="collection")
    @patch.object(CallRecord, "__init__", return_value=None)
    def test_build_call_record(self, mock_repo_init, mock_getter):
        actual = builders.build_call_record()

        mock_getter.assert_called_once_with(constants.CALL_RECORD_COLLECTION)
        mock_repo_init.assert_called_once_with("collection")
        self.assertIsInstance(actual, CallRecord)

    @patch("app.repository.mongo.get_collection", return_value="collection")
    @patch.object(Call, "__init__", return_value=None)
    def test_build_call(self, mock_repo_init, mock_getter):
        actual = builders.build_call()

        mock_getter.assert_called_once_with(constants.CALL_RECORD_COLLECTION)
        mock_repo_init.assert_called_once_with("collection")
        self.assertIsInstance(actual, Call)

    @patch("app.repository.mongo.get_collection", return_value="collection")
    @patch.object(PhoneBill, "__init__", return_value=None)
    def test_phone_bill(self, mock_repo_init, mock_getter):
        actual = builders.build_phone_bill()

        mock_getter.assert_called_once_with(constants.PHONE_BILL_COLLECTION)
        mock_repo_init.assert_called_once_with("collection")
        self.assertIsInstance(actual, PhoneBill)
