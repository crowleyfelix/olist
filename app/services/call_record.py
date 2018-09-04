"""Module with call record service."""
import logging
from app import mongo

LOGGER = logging.getLogger(__name__)


class CallRecord(object):
    """Class for call record operations."""

    def __init__(self):
        """Initialize attributes."""
        self.collection = mongo.CallRecord()

    def create(self, record):
        """Add call record."""
        LOGGER.debug("Creating call record")
        return self.collection.add(record)
