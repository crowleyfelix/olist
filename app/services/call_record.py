"""Module with call record service."""
import logging
from app import repository

LOGGER = logging.getLogger(__name__)


class CallRecord(object):
    """Class for call record operations."""

    def __init__(self):
        """Initialize attributes."""
        self.repository = repository.build_call_record()

    def create(self, record):
        """Add call record."""
        LOGGER.debug("Creating call record")
        return self.repository.add(record)
