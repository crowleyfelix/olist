from unittest import TestCase
from unittest.mock import patch
from app.repository import mongo


class TestMongo(TestCase):
    @patch("pymongo.MongoClient")
    def test_get_collection(self, mock_client):
        col1 = mongo.get_collection("col")
        col2 = mongo.get_collection("col")
        self.assertEqual(col1, col2)
