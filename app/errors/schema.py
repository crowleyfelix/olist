"""Module with a schema error."""
from .error import Error


class SchemaError(Error):
    """Represents a schema error."""

    def __init__(self, message=None):
        """Initialize attributes."""
        messages = ["Invalid data passed"]
        super(SchemaError, self).__init__(messages, 400)
