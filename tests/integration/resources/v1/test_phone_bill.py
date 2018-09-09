import json
from tests.integration.base import BaseSuite
from app import services
from app.application import Application
from app.repository import mongo, constants
from app.models.enums import CallRecordType
from . import fixtures

GET_ENDPOINT = "/api/v1/phones/{phone_number}/bills"


class TestPhoneBill(BaseSuite):
    def setUp(self):
        records = [
            fixtures.call_record_start(),
            fixtures.call_record_end()
        ]

        service = services.build_call_record()
        for record in records:
            record["type"] = CallRecordType(record["type"])
            service.create(record)

        self.engine = Application.build_engine()

    def test_get(self):
        phone_number = "99988526423"
        period = "2018-03"

        with self.subTest("when not found bill"):
            url = GET_ENDPOINT.format(phone_number="3")
            url += f"?period={period}"
            _, response = self.engine.test_client.get(url)
            self.assertEqual(response.status, 404)

        with self.subTest("when found bill"):
            url = GET_ENDPOINT.format(phone_number=phone_number)
            url += f"?period={period}"

            expected = fixtures.phone_bill()
            _, response = self.engine.test_client.get(url)

            self.assertEqual(response.status, 200)
            actual = response.json["data"]
            expected.update(id=actual[0]["id"])

            self.assertEqual(actual, [expected])

        with self.subTest("when period is invalid"):
            url = GET_ENDPOINT.format(phone_number=phone_number)
            url += f"?period=teste"

            _, response = self.engine.test_client.get(url)
            self.assertEqual(response.status, 400)

        with self.subTest("when exceeds pages"):
            url = GET_ENDPOINT.format(phone_number=phone_number)
            url += f"?period={period}&page=2"
            _, response = self.engine.test_client.get(url)

            self.assertEqual(response.status, 404)

    def tearDown(self):
        mongo.get_collection(constants.CALL_RECORD_COLLECTION).delete_many({})
        mongo.get_collection(constants.PHONE_BILL_COLLECTION).delete_many({})
