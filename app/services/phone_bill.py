"""Module with bill service."""
from app import mongo
from app.processors import billing
from app.utils import datetime


class PhoneBill(object):
    """Class for billing operations."""

    def __init__(self):
        """Initialize attributes."""
        self.collection = mongo.CallRecord()

    def get(self, phone_number, period=None):
        """Get phone bill."""
        start_date = None
        end_date = None

        if not period:
            start_date, end_date = datetime.begin_end_previous_month()
        else:
            start_date, end_date = datetime.begin_end_month(period)

        documents = self.collection.search(phone_number, start_date, end_date)

        calls = []
        for call in documents:

            start_date = datetime.from_timestamp(call["start_timestamp"])
            end_date = datetime.from_timestamp(call["end_timestamp"])
            call["amount"] = billing.process_call(
                start_date, end_date)

            calls.append(call)

        return calls
