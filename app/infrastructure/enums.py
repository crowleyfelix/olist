"""Module with infrastructure enums."""
from enum import Enum


class AppMode(Enum):
    """Enum of application mode."""

    DEBUG = 1
    RELEASE = 2
    TEST = 3
