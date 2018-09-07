"""Module that contains configuration helpers."""
import os
from munch import Munch
from .enums import AppMode

_CONFIG = Munch()

LOG_FORMAT = "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"
DATETIME_FORMAT = "%m-%d %H:%M"
ROOT_PATH = os.path.join(
    os.path.pardir, os.path.dirname(__file__),
    os.path.pardir,
    os.path.pardir)


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

    queries_path = os.path.abspath(
        os.path.join(ROOT_PATH, "static", "queries"))

    _CONFIG.update(
        mode=AppMode(int(env.get("MODE", AppMode.DEBUG.value))),
        host=env.get("HOST", "0.0.0.0"),
        port=env.get("PORT", 8000),
        queries_path=env.get("QUERIES_PATH", queries_path),

        logging=Munch(
            level=env.get("LOGGING_LEVEL", "DEBUG"),
            format=env.get("LOGGING_FORMAT", LOG_FORMAT),
            datefmt=env.get("LOGGING_DATEFORMAT", DATETIME_FORMAT)
        ),

        mongo=Munch(
            uri=env["MONGO_URI"],
            database=env["MONGO_DATABASE"]
        )
    )


def set_test_mode():
    """Set application test mode."""
    config = get_config()
    config.mode = AppMode.TEST
