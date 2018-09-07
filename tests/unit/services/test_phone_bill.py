from datetime import datetime
from unittest import TestCase
from unittest.mock import patch, Mock
from app.services.phone_bill import PhoneBill


class TestPhoneBill(TestCase):

    @patch("app.repository.build_call")
    @patch("app.repository.build_phone_bill")
    def setUp(self, mock_bill_builder, mock_call_builder):
        self.mock_bill_repository = mock_bill_builder()
        self.mock_call_repository = mock_call_builder()
        PhoneBill._instance = None
        self.service = PhoneBill()

    @patch("app.processors.paging.filter")
    @patch("app.processors.paging.process")
    def test_list(self, mock_page_processor, mock_page_filter):
        phone_number = 1
        period = "2016-02"
        page = 2
        limit = 3
        bill = [1, 2, 3, 4]

        self.service._get = Mock()
        self.service._generate_bill = Mock()
        self.service.create = Mock()

        with self.subTest("when no bill found on first page"):
            self.service._get.return_value = (None, {"size": 0, "current": 1})
            self.service._generate_bill.return_value = bill
            mock_page_processor.return_value = "page"
            self.service.create.return_value = bill
            mock_page_filter.return_value = "filtered"

            actual = self.service.list(
                phone_number, period, page, limit)

            self.service._generate_bill.assert_called_once_with(phone_number,
                                                                period)

            mock_page_processor.assert_called_once_with(page, limit, len(bill))
            self.service.create.assert_called_once_with(bill)
            mock_page_filter.assert_called_once_with(bill, page, limit)
            self.assertEqual(actual, ("filtered", "page"))

        with self.subTest("when found on first page"):
            self.service._get.return_value = bill, {"size": 1, "current": 1}

            actual = self.service.list(
                phone_number, period, page, limit)

            self.assertEqual(actual, (bill, {"size": 1, "current": 1}))

    def test__get(self):
        phone_number = 1
        period = "2016-02"
        page = 2
        limit = 3
        self.mock_bill_repository.search.return_value = "data"
        actual = self.service._get(phone_number, period, page, limit)
        self.mock_bill_repository.search.assert_called_once_with(
            phone_number, period, page, limit)
        self.assertEqual(actual, "data")

    @patch("app.processors.billing.process", return_value="processed")
    @patch("app.utils.datetime.begin_end_month")
    @patch("app.utils.datetime.begin_end_previous_month")
    def test__generate_bill(self, mock_datetime_previous_month,
                            mock_datetime_begin_end,
                            mock_processor):
        phone_number = 1
        period = "2016-02"

        with self.subTest("when period is empty"):
            self.mock_call_repository.search.return_value = "calls"
            now = datetime.now()
            mock_datetime_previous_month.return_value = (now, now)

            actual = self.service._generate_bill(phone_number, None)

            self.mock_call_repository.search.assert_called_once_with(
                phone_number, now, now)
            mock_processor.assert_called_once_with(
                "calls", f"{now.year}-{now.month}")
            self.assertEqual(actual, "processed")

    def test_create(self):
        self.mock_bill_repository.add.return_value = "added"
        actual = self.service.create("record")
        self.assertEqual(actual, "added")
