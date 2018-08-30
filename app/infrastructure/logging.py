"""Module with log bootstrap."""
import logging
from .configuration import get_config


def setup():
    """Build logging engine."""
    config = get_config()
    logging.basicConfig(**config.logging)
