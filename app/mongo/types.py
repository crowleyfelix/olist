"""Module for mongo types."""


class Documents(object):
    """Wrapper for mongo cursor."""

    def __init__(self, cursor):
        """Initialize attributes."""
        self._cursor = cursor

    def __iter__(self):
        """Get iterable."""
        return self

    def __next__(self):
        """Get next value."""
        try:
            return Document(self._cursor.next())
        except StopIteration as ex:
            self._cursor.close()
            raise ex


class Document(dict):
    """Wrapper for mongo document."""

    def __init__(self, raw):
        """Initialize attributes."""
        raw.pop("_id")
        self.update(**raw)
