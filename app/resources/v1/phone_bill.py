"""Module that contains call record resources."""
from app import services
from app.infrastructure import web
from .contracts import build_response
from app.services.phone_bill import DEFAULT_PAGE, DEFAULT_LIMIT


def register(blueprint):
    """Register call records namespace."""
    blueprint.add_route(get, "/phone/<phone_number>/bill")


async def get(request, phone_number):
    """Get phone bill."""
    service = services.PhoneBill()

    period = request.args.get("period")
    page = int(request.args.get("page", DEFAULT_PAGE))
    size = int(request.args.get("page_size", DEFAULT_LIMIT))

    bill, page_info = service.list(phone_number, period, page, size)
    return web.json(build_response(bill, page_info))
