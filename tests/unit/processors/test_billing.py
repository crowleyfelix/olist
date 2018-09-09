from datetime import datetime
from unittest import TestCase
from unittest.mock import patch, Mock
from app.processors import billing
from app.models.enums import ChargeStrategy
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


def mock_is_between_time_return(expected_cycle):
    def f(start_date, start_cycle, end_cycle):
        if (start_cycle, end_cycle) == expected_cycle:
            return True

        return False

    return f


class TestBilling(TestCase):
    def setUp(self):
        self.original_charges = billing.CALL_CHARGES
        billing.CALL_CHARGES = MOCK_CHARGES

    @patch("app.processors.billing.calculate_price", return_value="calculated")
    @patch("app.utils.datetime.from_timestamp", return_value="datetime")
    def test_process(self, mock_timestamp_parser, mock_price_calculator):
        calls = [{"start_timestamp": "start_timestamp",
                  "end_timestamp": "end_timestamp"}]

        actual = billing.process(calls, "period")

        expected = [{"start_timestamp": "start_timestamp",
                     "end_timestamp": "end_timestamp",
                     "price": "calculated",
                     "period": "period"}]

        mock_timestamp_parser.assert_any_call("start_timestamp")
        mock_timestamp_parser.assert_any_call("end_timestamp")
        mock_price_calculator.assert_called_once_with(
            "datetime", "datetime", ChargeStrategy.homogeneous)
        self.assertEqual(actual, expected)

    @patch("app.utils.datetime.get_cycle_ocurrencies")
    def test__calculate_heterogeneous_price(self, mock_cycle_calculator: Mock):
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
            actual = billing._calculate_heterogeneous_price(
                start_date, end_date)

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
            actual = billing._calculate_heterogeneous_price(
                start_date, end_date)

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
            actual = billing._calculate_heterogeneous_price(
                start_date, end_date)

            self.assertEqual(actual, expected)

    @patch("app.utils.datetime.is_between_time")
    def test__calculate_homogeneous_price(self, mock_is_between_time):
        start_date = parse_datetime("2018-02-28T10:00:13Z")
        end_date = parse_datetime("2018-02-28T10:03:12Z")

        with self.subTest("when appear in first cycle"):
            charge = MOCK_CHARGES[0]
            cycle = (charge["start"], charge["end"])

            mock_is_between_time.side_effect = mock_is_between_time_return(
                cycle)

            expected = billing.DEFAULT_FIXED_CHARGE + 18
            actual = billing._calculate_homogeneous_price(
                start_date, end_date)

            self.assertEqual(actual, expected)

        with self.subTest("when appear in seccond cycle"):
            charge = MOCK_CHARGES[1]
            cycle = (charge["start"], charge["end"])

            mock_is_between_time.side_effect = mock_is_between_time_return(
                cycle)

            expected = billing.DEFAULT_FIXED_CHARGE + 2
            actual = billing._calculate_homogeneous_price(
                start_date, end_date)

            self.assertEqual(actual, expected)

    def tearDown(self):
        billing.CALL_CHARGES = self.original_charges
