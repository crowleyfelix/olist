"""Module with phone bill repository."""
from pymongo.errors import DuplicateKeyError
from app.infrastructure.singleton import Singleton
from app import errors
from app.processors import paging
from .types import Documents
from . import query, schema


class PhoneBill(metaclass=Singleton):
    """A repository phone bill operations."""

    def __init__(self, collection):
        """Initialize private attributes."""
        self._collection = collection

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

        count = self._collection.count_documents(builded_query)

        page_info = paging.process(page, limit, count)

        return (documents, page_info)
