from unittest import TestCase
from unittest.mock import patch
from app.repository import mongo
from . import fixtures


class TestMongo(TestCase):
    @patch("app.repository.mongo.get_config")
    @patch("pymongo.MongoClient")
    def test_get_collection(self, mock_client, mock_config_getter):
        mock_config = fixtures.config()
        mock_config_getter.return_value = mock_config

        with self.subTest("when is in test mode"):
            col1 = mongo.get_collection("col")
            col2 = mongo.get_collection("col")

            self.assertEqual(col1, col2)
            self.assertEqual(col2, mock_client()["test"]["col"])

        mongo._COLLECTIONS = {}
        mock_config.mode = 1
        with self.subTest("when is not in test mode"):
            col1 = mongo.get_collection("col")
            col2 = mongo.get_collection("col")

            self.assertEqual(col1, col2)
            self.assertEqual(col2, mock_client()[
                             mock_config.mongo.database]["col"])
