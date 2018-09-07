"""Module with phone bill repository."""
from pymongo.errors import DuplicateKeyError
from app import errors
from app.processors import paging
from .engine import get_collection
from .types import Documents
from . import query, schema, constants


class PhoneBill(object):
    """A repository phone bill operations."""

    def __init__(self):
        """Initialize private attributes."""
        self._collection = get_collection(constants.PHONE_BILL_COLLECTION)

    def add(self, bill):
        """Add start or end bill."""
        bill_schema = schema.PHONE_BILL
        bill = schema.parse(bill, [bill_schema])
        try:
            self._collection.insert_many(bill)
            return Documents(iter(bill), bill_schema)
        except DuplicateKeyError:
            raise errors.UnprocessableDataError("Phone bill already exists")

    def search(self, phone_number, period, page, limit):
        """Search by call records."""
        bill_schema = schema.PHONE_BILL
        builded_query = query.build(query.FIND_PHONE_BILL,
                                    phone_number=phone_number,
                                    period=period)

        documents = Documents(self._collection.find(builded_query),
                              bill_schema,
                              page,
                              limit)

        count = self._collection.count(builded_query)

        page_info = paging.process(page, limit, count)

        return (documents, page_info)
