"""Module with a schema error."""
from .error import Error


class SchemaError(Error):
    """Represents a schema error."""

    def __init__(self, message=None, glom_error=None):
        """Initialize attributes."""
        messages = ["Invalid data passed"]

        if glom_error:
            messages = glom_error.msgs
        elif message:
            messages = [message]

        super(SchemaError, self).__init__(messages, 400)
