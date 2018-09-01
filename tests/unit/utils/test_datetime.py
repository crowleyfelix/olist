from datetime import datetime
from unittest import TestCase
from app.utils.datetime import get_cycle_ocurrencies
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

                actual = get_cycle_ocurrencies(
                    start_range, end_range, start_cycle, end_cycle)

                self.assertEqual(actual, expected)
