import json
from unittest import TestCase
from app.infrastructure.web import Engine, Blueprint
from app.application import Application
from app.resources.v1 import call_record
from . import fixtures

POST_ENDPOINT = "/v1/call-records"


class TestCallRecord(TestCase):
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
                self.assertEqual(response.json["data"], pld)
