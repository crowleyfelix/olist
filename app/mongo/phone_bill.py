"""Module with phone bill repository."""
from .engine import get_collection
from .types import Documents
from . import query

COLLECTION_NAME = "phoneBill"


class PhoneBill(object):
    """A repository phone bill operations."""

    def __init__(self):
        """Initialize private attributes."""
        self._collection = get_collection(COLLECTION_NAME)

    def add(self, bill):
        """Add start or end bill."""
        self._collection.insert_many(bill)
        return Documents(bill)

    def search(self, phone_number, period, page, limit):
        """Search by call records."""
        builded_query = query.build(query.FIND_PHONE_BILL,
                                    phone_number=phone_number,
                                    period=period)

        return Documents(self._collection.find(builded_query), page, limit)