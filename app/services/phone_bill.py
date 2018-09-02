"""Module with bill service."""
from app import mongo
from app.processors import billing
from app.utils import datetime


class PhoneBill(object):
    """Class for billing operations."""

    def __init__(self):
        """Initialize attributes."""
        self.call_collection = mongo.CallRecord()
        self.bill_collection = mongo.PhoneBill()

    def list(self, phone_number, period=None, page=1, limit=10):
        """Get phone bill."""
        bill = self._get(phone_number, period, page, limit)
        bill = list(bill)

        if not bill:
            bill = self._generate_bill(phone_number, period)

            if bill:
                bill = self.create(bill)

                bill = self._filter_page(bill, page, limit)

        return bill

    def _get(self, phone_number, period, page, limit):
        return self.bill_collection.search(phone_number, period, page, limit)

    def _generate_bill(self, phone_number, period):
        start_date = None
        end_date = None

        if not period:
            start_date, end_date = datetime.begin_end_previous_month()

            # TODO: Define period
        else:
            start_date, end_date = datetime.begin_end_month(period)

        documents = self.call_collection.search(
            phone_number, start_date, end_date)

        bill = []
        for call in documents:

            start_date = datetime.from_timestamp(call["start_timestamp"])
            end_date = datetime.from_timestamp(call["end_timestamp"])
            call["price"] = billing.process_call(
                start_date, end_date)
            call["period"] = period

            bill.append(call)

        return bill

    def create(self, bill):
        """Create bill."""
        return self.bill_collection.add(bill)

    def _filter_page(self, items, page, limit):
        offset = (page-1) * limit
        return items[offset:offset-1]
