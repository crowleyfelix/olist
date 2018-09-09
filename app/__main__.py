"""Application package entry point."""
from app.infrastructure import setup_log
from .application import Application

setup_log()
Application().start()
