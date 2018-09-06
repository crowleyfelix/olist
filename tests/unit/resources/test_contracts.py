from unittest import TestCase
from app.resources import contracts


class TestContracts(TestCase):
    def test_build_response(self):
        actual = contracts.build_response({"test": 1}, {"current": 1}, ["abc"])
        self.assertEqual(actual, {
            "data": {
                "test": 1,

            },
            "messages": ["abc"],
            "current": 1
        })

        self.assertEqual(contracts.build_response(),
                         {"data": {}, "messages": []})
