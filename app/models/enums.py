"""Module with domain enums."""
from enum import Enum


class CallRecordType(Enum):
    """Enumerator of call record type."""

    start = "start"
    end = "end"
