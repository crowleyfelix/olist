"""Module with call record repository."""
from .engine import get_collection
from .query_builders import CallRecord as builder
from .types import List

COLLECTION_NAME = "callRecord"


class CallRecord(object):
    """A repository for call record operations."""

    def __init__(self):
        """Initialize private attributes."""
        self._collection = get_collection(COLLECTION_NAME)

    def add(self, record):
        """Add start or end record."""
        self._collection.insert_one(record)
        record.pop('_id')

        return record

    def search(self, phone_number, start_date, end_date):
        """Search by call records."""
        start_timestamp = start_date.timestamp()
        end_timestamp = end_date.timestamp()

        query = builder.by_billing_cycle(phone_number,
                                         start_timestamp,
                                         end_timestamp)
        return List(self._collection.find(query))
