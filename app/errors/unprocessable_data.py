"""Module with unprocessable data error."""
from .error import Error


class UnprocessableDataError(Error):
    """Represents an unprocessable data error."""

    def __init__(self, message):
        """Call parent to initialize attributes."""
        super(UnprocessableDataError, self).__init__(message, 422)
