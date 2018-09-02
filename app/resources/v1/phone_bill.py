"""Module that contains call record resources."""
from app import services
from app.infrastructure import web


def register(blueprint):
    """Register call records namespace."""
    blueprint.add_route(get, "/phone/<phone_number>/bill")


async def get(request, phone_number):
    """Get phone bill."""
    service = services.PhoneBill()

    period = request.args.get("period")

    bill = service.list(phone_number, period)
    return web.json(bill)
