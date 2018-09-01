from datetime import datetime
from unittest import TestCase
from unittest.mock import patch, Mock
from app.processors import billing
from tests.utils import parse_datetime, parse_time

MOCK_CHARGES = [{
    "value": 9,
    "start": parse_time("10:00"),
    "end": parse_time("11:00")
}, {
    "value": 1,
    "start": parse_time("23:00"),
    "end": parse_time("00:30")
}]


def mock_cycle_calculator_return(expected_cycles, return_value):
    def f(start_date, end_date, start_cycle, end_cycle):
        if (start_cycle, end_cycle) in expected_cycles:
            return return_value

        return []

    return f


class TestBilling(TestCase):
    def setUp(self):
        self.original_charges = billing.CALL_CHARGES
        billing.CALL_CHARGES = MOCK_CHARGES

    @patch("app.utils.datetime.get_cycle_ocurrencies")
    def test_process_call(self, mock_cycle_calculator: Mock):
        start_date = "start_date"
        end_date = "end_date"

        with self.subTest("when appear in first cycle"):
            charge = MOCK_CHARGES[0]
            cycles = [
                (charge["start"], charge["end"])
            ]

            return_value = [
                (parse_datetime("2018-02-28T10:00:13Z"),
                 parse_datetime("2018-02-28T10:03:12Z"))
            ]

            mock_cycle_calculator.side_effect = mock_cycle_calculator_return(
                cycles, return_value)

            expected = billing.DEFAULT_FIXED_CHARGE + 18
            actual = billing.process_call(start_date, end_date)

            self.assertEqual(actual, expected)

        with self.subTest("when appear in second cycle"):
            charge = MOCK_CHARGES[1]
            cycles = [
                (charge["start"], charge["end"])
            ]

            return_value = [
                (parse_datetime("2018-02-28T23:59:13Z"),
                 parse_datetime("2018-03-01T00:02:12Z"))
            ]

            mock_cycle_calculator.side_effect = mock_cycle_calculator_return(
                cycles, return_value)

            expected = billing.DEFAULT_FIXED_CHARGE + 2
            actual = billing.process_call(start_date, end_date)

            self.assertEqual(actual, expected)

        with self.subTest("when appear in both cycles"):
            cycles = []
            for charge in MOCK_CHARGES:
                cycles.append((charge["start"], charge["end"]))

            return_value = [
                (parse_datetime("2018-02-28T10:00:13Z"),
                 parse_datetime("2018-02-28T10:03:12Z")),
            ]

            mock_cycle_calculator.side_effect = mock_cycle_calculator_return(
                cycles, return_value)

            expected = billing.DEFAULT_FIXED_CHARGE + 20
            actual = billing.process_call(start_date, end_date)

            self.assertEqual(actual, expected)

    def tearDown(self):
        billing.CALL_CHARGES = self.original_charges
