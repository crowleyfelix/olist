"""Module that contains routes register."""
from sanic import Sanic, Blueprint
from . import call_record


def register(engine: Sanic):
    """Register routes."""
    blueprint = Blueprint("v1", url_prefix="/v1")
    call_record.register(blueprint)
    engine.register_blueprint(blueprint)
