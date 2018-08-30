"""Module that contains register resource routes."""
import logging
from . import (health_check,
               exception,
               v1)

LOGGER = logging.getLogger(__name__)


def register(engine):
    """Register resources routes."""
    logging.debug("Registering routes...")

    health_check.register(engine)
    v1.register(engine)
    exception.register(engine)
