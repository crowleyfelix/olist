"""Module with call record service."""
from app import mongo


class CallRecord(object):
    """Class for call record operations."""

    def __init__(self):
        """Initialize attributes."""
        self.collection = mongo.CallRecord()

    def create(self, record):
        """Add call record."""
        result = self.collection.add(record)
        return result
