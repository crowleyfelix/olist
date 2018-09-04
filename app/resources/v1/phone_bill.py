"""Module that contains call record resources."""
from app import services
from app.resources.contracts import auto_parse
from . import contracts


def register(blueprint):
    """Register call records namespace."""
    blueprint.add_route(get, "/phone/<phone_number>/bill")


@auto_parse(contracts.PHONE_BILL_REQUEST, {})
async def get(params):
    """Get phone bill."""
    service = services.PhoneBill()
    return service.list(params.phone_number,
                        params.period,
                        params.page,
                        params.limit)
