"""Module for mongo types."""


class List(object):
    """List cursor."""

    def __init__(self, cursor):
        """Initialize attributes."""
        self._cursor = cursor

    def __iter__(self):
        """Get iterable."""
        return self

    def __next__(self):
        """Get next value."""
        try:
            document = self._cursor.next()
            document.pop("_id")
            return document
        except StopIteration as ex:
            self._cursor.close()
            raise ex
