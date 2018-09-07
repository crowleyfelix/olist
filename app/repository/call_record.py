"""Module with call record repository."""
from pymongo.errors import DuplicateKeyError
from app import errors
from . import schema
from .types import Document


class CallRecord(object):
    """A repository for call record operations."""

    def __init__(self, collection):
        """Initialize private attributes."""
        self._collection = collection

    def add(self, record):
        """Add start or end record."""
        record_schema = schema.CALL_RECORD[record["type"]]
        record = schema.parse(record, record_schema)
        try:
            self._collection.insert_one(record)
            return Document(record, record_schema)
        except DuplicateKeyError:
            raise errors.UnprocessableDataError("Call record already exists")
