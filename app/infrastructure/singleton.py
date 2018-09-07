"""Module with singleton metaclass."""


class Singleton(type):
    """Type singleton for unique instances."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Get current instance."""
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
