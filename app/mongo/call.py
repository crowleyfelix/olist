"""Module with call repository."""
from . import query, constants, schema
from .engine import get_collection
from .types import Documents


class Call(object):
    """A repository for call operations."""

    def __init__(self):
        """Initialize private attributes."""
        self._collection = get_collection(constants.CALL_RECORD_COLLECTION)

    def search(self, phone_number, start_date, end_date):
        """Search by call records."""
        start_timestamp = start_date.timestamp()
        end_timestamp = end_date.timestamp()

        call_schema = schema.CALL
        builded_query = query.build(query.LIST_CALLS,
                                    source=phone_number,
                                    start_timestamp=start_timestamp,
                                    end_timestamp=end_timestamp)

        return Documents(self._collection.aggregate(builded_query),
                         call_schema)
