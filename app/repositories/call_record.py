"""Module with call record repository."""
from .mongo import get_collection

COLLECTION_NAME = "callRecord"


class CallRecord(object):
    """A repository for call record operations."""

    def __init__(self):
        """Initialize private attributes."""
        self._collection = get_collection(COLLECTION_NAME)

    def add_record(self, record):
        """Add start or end record."""
        self._collection.insert_one(record)
        record.pop('_id')
