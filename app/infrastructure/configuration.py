"""Module that contains configuration helpers."""
import os
from munch import Munch
from .enums import AppMode

_CONFIG = Munch()

LOG_FORMAT = "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"
DATETIME_FORMAT = "%m-%d %H:%M"


def get_config():
    """Get application configuration."""
    if not _CONFIG:
        try:
            _load_config()
        except KeyError as e:
            print(f"Missing {e} configuration")
            raise e

    return _CONFIG


def _load_config():
    env = os.environ

    _CONFIG.update(
        mode=AppMode(int(env.get("MODE", AppMode.DEBUG.value))),
        host=env.get("HOST", "0.0.0.0"),
        port=env.get("PORT", 8000),

        logging=Munch(
            level=env.get("LOGGING_LEVEL", "DEBUG"),
            format=env.get("LOGGING_FORMAT", LOG_FORMAT),
            datefmt=env.get("LOGGING_DATEFORMAT", DATETIME_FORMAT)
        )
    )
