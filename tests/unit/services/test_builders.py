from unittest import TestCase
from unittest.mock import patch
from app.services import builders
from app.services.call_record import CallRecord
from app.services.phone_bill import PhoneBill


class TestBuilders(TestCase):
    def setUp(self):
        CallRecord._instance = None
        PhoneBill._instance = None

    def test_build_call_record(self):
        actual = builders.build_call_record()
        self.assertIsInstance(actual, CallRecord)

    def test_phone_bill(self):
        actual = builders.build_phone_bill()
        self.assertIsInstance(actual, PhoneBill)
