"""Module for mongo types."""
from . import schema


class Documents(object):
    """Wrapper for mongo cursor."""

    def __init__(self, cursor, schema, page=None, limit=None):
        """Initialize attributes."""
        if page and limit:
            offset = (page-1)*limit
            cursor = cursor.skip(offset).limit(limit)

        self._cursor = cursor
        self._schema = schema

    def __iter__(self):
        """Get iterable."""
        return self

    def __next__(self):
        """Get next value."""
        try:
            return Document(next(self._cursor), self._schema)
        except StopIteration as ex:
            if hasattr(self._cursor, "close"):
                self._cursor.close()
            raise ex


class Document(dict):
    """Wrapper for mongo document."""

    def __init__(self, raw, doc_schema):
        """Initialize attributes."""
        self.update(**schema.parse(raw, doc_schema))
