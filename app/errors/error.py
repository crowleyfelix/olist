"""Module with app base custom error."""


class Error(Exception):
    """Base custom error."""

    def __init__(self, messages, status_code):
        """Initialize attributes."""
        if not isinstance(messages, list):
            messages = [messages]
        self.messages = messages
        self.status_code = status_code

        super(Error, self).__init__(' | '.join(messages))
