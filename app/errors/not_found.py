"""Module with a not found error."""
from .error import Error


class NotFoundError(Error):
    """Represents a not found error."""

    def __init__(self, message=None):
        """Initialize attributes."""
        message = message or "Not found"
        super(NotFoundError, self).__init__(message, 404)
