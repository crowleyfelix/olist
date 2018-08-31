from datetime import datetime
from unittest import TestCase
from app.utils.date_time import DateTimeCycle
from . import fixtures


class TestDateTimeCycle(TestCase):
    def test_get_cycle_ocurrencies(self):
        with self.subTest("with standard cycle"):
            start_range = fixtures.START_RANGE
            end_range = fixtures.END_RANGE
            start_cycle = fixtures.STANDARD_CYCLE["start"]
            end_cycle = fixtures.STANDARD_CYCLE["end"]
            expected = fixtures.STANDARD_CYCLE["ocurrencies"]

            actual = DateTimeCycle.get_cycle_ocurrencies(
                start_range, end_range, start_cycle, end_cycle)

            self.assertEqual(actual, expected)

        with self.subTest("with reduced cycle"):
            start_range = fixtures.START_RANGE
            end_range = fixtures.END_RANGE
            start_cycle = fixtures.REDUCED_CYCLE["start"]
            end_cycle = fixtures.REDUCED_CYCLE["end"]
            expected = fixtures.REDUCED_CYCLE["ocurrencies"]

            actual = DateTimeCycle.get_cycle_ocurrencies(
                start_range, end_range, start_cycle, end_cycle)

            self.assertEqual(actual, expected)
