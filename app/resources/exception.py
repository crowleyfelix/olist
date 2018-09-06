"""Module with exception handling logic."""
import logging
import traceback
from app.infrastructure import web
from app.infrastructure.configuration import get_config
from app.infrastructure.enums import AppMode
from http import HTTPStatus
from . import contracts

LOGGER = logging.getLogger(__name__)


def register(engine):
    """Register exception handler."""
    engine.exception(Exception)(handle_all)


def handle_all(request, exception):
    """Handle all api exceptions."""
    messages = [str(exception)]

    LOGGER.warning(f"Handling with exception raised {exception}")

    if hasattr(exception, "status_code"):
        status_code = exception.status_code
    elif hasattr(exception, "code"):
        status_code = exception.code
    else:
        config = get_config()

        if config.mode is AppMode.DEBUG:
            messages.append(traceback.format_exc())
        else:
            messages = [HTTPStatus.INTERNAL_SERVER_ERROR.name]

        LOGGER.error("Unknown exception raised "
                     f"[Type] {type(exception)} "
                     f"[Message] {exception}")
        status_code = 500

    response = contracts.build_response(messages=messages)

    return web.json(response,
                    status_code)
