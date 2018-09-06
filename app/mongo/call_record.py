"""Module with call record repository."""
from . import schema
from .engine import get_collection
from .types import Document

COLLECTION_NAME = "callRecord"


class CallRecord(object):
    """A repository for call record operations."""

    def __init__(self):
        """Initialize private attributes."""
        self._collection = get_collection(COLLECTION_NAME)

    def add(self, record):
        """Add start or end record."""
        record = schema.parse(record, schema.CALL_RECORD[record["type"]])
        self._collection.insert_one(record)
        return Document(record)
