"""Module that contains register resource routes."""
import logging
from . import (health_check,
               exception)

LOGGER = logging.getLogger(__name__)


def register(engine):
    """Register resources routes."""
    logging.debug("Registering routes...")
    health_check.register(engine)
    exception.register(engine)
