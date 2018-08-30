"""Module with exception handling logic."""
import logging
from app.infrastructure import web

LOGGER = logging.getLogger(__name__)


def register(engine):
    """Register exception handler."""
    engine.exception(Exception)(handle_all)


def handle_all(request, exception):
    """Handle all api exceptions."""
    if hasattr(exception, "status_code"):
        status_code = exception.status_code
    else:
        LOGGER.error("Unknown exception raised "
                     f"[Type] {type(exception)} "
                     f"[Message] {exception}")
        status_code = 500

    return web.json({"message": str(exception)},
                    status_code)
