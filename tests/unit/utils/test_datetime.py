from unittest import TestCase
from unittest.mock import patch
from app.utils import datetime
from . import fixtures


class TestDateTime(TestCase):
    def test_get_cycle_ocurrencies(self):
        start_range = fixtures.START_RANGE
        end_range = fixtures.END_RANGE

        cycles = [fixtures.STANDARD_CYCLE, fixtures.REDUCED_CYCLE]

        for cycle in cycles:
            start_cycle = cycle["start"]
            end_cycle = cycle["end"]
            expected = cycle["ocurrencies"]

            with self.subTest(f"when start at {start_cycle} "
                              f"and end at {end_cycle}"):

                actual = datetime.get_cycle_ocurrencies(
                    start_range, end_range, start_cycle, end_cycle)

                self.assertEqual(actual, expected)

    def test_to_datetime(self):
        actual = datetime.to_datetime("2018-02-28T21:57:13Z")
        self.assertNotIsInstance(actual, str)
        self.assertEqual(str(actual), "2018-02-28 21:57:13")

    def test_to_time(self):
        actual = datetime.to_time("21:57")
        self.assertNotIsInstance(actual, str)
        self.assertEqual(str(actual), "21:57:00")

    def test_begin_end_month(self):
        actual_start, actual_end = datetime.begin_end_month("2018-02")
        self.assertEqual(str(actual_start), "2018-02-01 00:00:00")
        self.assertEqual(str(actual_end), "2018-02-28 23:59:59")

    def test_diff_str(self):
        actual = datetime.diff_str(0, 60*60+(60+1))
        self.assertEqual(actual, "1h1m1s")
