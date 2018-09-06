"""Contains Application class."""
import logging
from app import resources
from app.infrastructure.web import Engine
from app.infrastructure.enums import AppMode
from app.infrastructure.configuration import get_config

LOGGER = logging.getLogger(__name__)


class Application(object):
    """Application is the class entry point to run current application."""

    def __init__(self):
        """Initialize application instance."""
        self.config = get_config()

    @staticmethod
    def build_engine():
        """Build web server engine."""
        engine = Engine(configure_logging=False)
        resources.register(engine)
        return engine

    def start(self):
        """Start the application."""
        LOGGER.info("Starting application")

        engine = self.build_engine()
        engine.run(self.config.host,
                   self.config.port,
                   debug=self.config.mode == AppMode.DEBUG,
                   access_log=True)
