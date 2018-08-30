"""Package with business logic services."""
from app import repositories


class CallRecord(object):
    """Class for call record operations."""

    def __init__(self):
        """Initialize repository."""
        self.repository = repositories.CallRecord()

    def add_record(self, record):
        """Add call record."""
        self.repository.add_record(record)
        return record
