import json
from tests.integration.base import BaseSuite
from app.infrastructure.web import Engine, Blueprint
from app.application import Application
from app.resources.v1 import call_record
from app.repository import mongo, constants
from . import fixtures

POST_ENDPOINT = "/api/v1/call-records"


class TestCallRecord(BaseSuite):
    def setUp(self):
        self.engine = Application.build_engine()

    def test_post(self):
        with self.subTest("with invalid payloads"):
            call_record_start = fixtures.call_record_start()
            call_record_start.pop("destination")

            payloads = [[],
                        {"type": "unknown"},
                        1,
                        "unknown",
                        {"timestamp": "test"},
                        call_record_start]

            for pld in payloads:
                data = json.dumps(pld)
                _, response = self.engine.test_client.post(POST_ENDPOINT,
                                                           data=data)

                self.assertEqual(response.status, 400)

        with self.subTest("with valid payloads"):
            payloads = [fixtures.call_record_end(),
                        fixtures.call_record_start()]

            for pld in payloads:
                data = json.dumps(pld)
                _, response = self.engine.test_client.post(POST_ENDPOINT,
                                                           data=data)

                self.assertEqual(response.status, 201)
                actual = response.json["data"]
                pld.update(id=actual["id"])
                self.assertEqual(actual, pld)

    def tearDown(self):
        collection = mongo.get_collection(constants.CALL_RECORD_COLLECTION)
        collection.delete_many({})
