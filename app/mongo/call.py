"""Module with call repository."""
from . import query
from .engine import get_collection
from .types import Documents

COLLECTION_NAME = "callRecord"


class Call(object):
    """A repository for call operations."""

    def __init__(self):
        """Initialize private attributes."""
        self._collection = get_collection(COLLECTION_NAME)

    def search(self, phone_number, start_date, end_date):
        """Search by call records."""
        start_timestamp = start_date.timestamp()
        end_timestamp = end_date.timestamp()

        builded_query = query.build(query.LIST_CALLS,
                                    source=phone_number,
                                    start_timestamp=start_timestamp,
                                    end_timestamp=end_timestamp)

        return Documents(self._collection.aggregate(builded_query))
