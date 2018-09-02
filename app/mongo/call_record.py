"""Module with call record repository."""
from . import query
from .engine import get_collection
from .types import Documents, Document

COLLECTION_NAME = "callRecord"


class CallRecord(object):
    """A repository for call record operations."""

    def __init__(self):
        """Initialize private attributes."""
        self._collection = get_collection(COLLECTION_NAME)

    def add(self, record):
        """Add start or end record."""
        self._collection.insert_one(record)
        return Document(record)

    def search(self, phone_number, start_date, end_date):
        """Search by call records."""
        start_timestamp = start_date.timestamp()
        end_timestamp = end_date.timestamp()

        builded_query = query.build(query.LIST_CALLS,
                                    source=phone_number,
                                    start_timestamp=start_timestamp,
                                    end_timestamp=end_timestamp)

        return Documents(self._collection.aggregate(builded_query))