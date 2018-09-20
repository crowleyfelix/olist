"""Module with bill service."""
import logging
from app import repository, errors
from app.processors import billing, validation
from app.utils import datetime
from app.processors import paging
from app.infrastructure.singleton import Singleton

LOGGER = logging.getLogger(__name__)


class PhoneBill(metaclass=Singleton):
    """Class for billing operations."""

    def __init__(self):
        """Initialize attributes."""
        self.call_repository = repository.build_call()
        self.bill_repository = repository.build_phone_bill()

    def list(self, phone_number, period, page, limit):
        """Get phone bill."""
        LOGGER.debug("Getting phone bill")

        bill, page_info = self._get(phone_number, period, page, limit)

        if not page_info["size"] and page_info["current"] == 1 and limit > 0:
            LOGGER.debug("No bill found on first page, generating new")

            bill = self._generate_bill(phone_number, period)
            page_info = paging.process(page, limit, len(bill))

            if bill:
                LOGGER.debug("Creating bill")
                bill = self.create(bill)

                LOGGER.debug("Filtering bill to requested page")
                bill = paging.filter(list(bill), page, limit)

        return (bill, page_info)

    def _get(self, phone_number, period, page, limit):
        return self.bill_repository.search(phone_number, period, page, limit)

    def _generate_bill(self, phone_number, period):
        start_date = None
        end_date = None

        if not period:
            LOGGER.debug("No period passed, getting previous month")
            start_date, end_date = datetime.begin_end_previous_month()
            period = f"{end_date.year}-{end_date.month}"
        else:
            LOGGER.debug(f"Generating bill for period {period} "
                         f"and phone number {phone_number}")
            if not validation.period_format(period):
                raise errors.SchemaError("Invalid period format")
            if not validation.closed_bill_period(period):
                raise errors.UnprocessableDataError("Period not closed")

            start_date, end_date = datetime.begin_end_month(period)

        calls = self.call_repository.search(
            phone_number, start_date, end_date)

        return billing.process(calls, period)

    def create(self, bill):
        """Create bill."""
        return self.bill_repository.add(bill)
