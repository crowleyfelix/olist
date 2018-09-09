"""Module with singleton metaclass."""


class Singleton(type):
    """Type singleton for unique instances."""

    def __init__(cls, name, bases, attrs, **kwargs):
        """Instantiate attributes."""
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        """Get current instance."""
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance
