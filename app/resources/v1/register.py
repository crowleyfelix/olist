"""Module that contains routes register."""
from sanic import Sanic, Blueprint
from . import call_record, phone_bill


def register(engine: Sanic):
    """Register routes."""
    blueprint = Blueprint(__name__, url_prefix="/v1")
    call_record.register(blueprint)
    phone_bill.register(blueprint)
    engine.register_blueprint(blueprint)
