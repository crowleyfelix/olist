"""Module with bill service."""
from app import mongo
from datetime import datetime
from dateutil.relativedelta import relativedelta


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
            today = datetime.today()
            period = f"{today.year}{today.month}"

            start_date = datetime.strptime(period, "%Y%m")
            start_date = start_date - relativedelta(months=1)
        else:
            start_date = datetime.strptime(period, "%Y%m")

        end_date = start_date + relativedelta(months=1, days=-1)

        result = self.collection.search(phone_number, start_date, end_date)
        return result
