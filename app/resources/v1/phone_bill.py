"""Module that contains call record resources."""
import logging
from app import services
from app.resources.contracts import auto_parse
from . import contracts

LOGGER = logging.getLogger(__name__)


def register(blueprint):
    """Register call records namespace."""
    blueprint.add_route(get, "/phone/<phone_number>/bill/<period>")


@auto_parse(contracts.PHONE_BILL_REQUEST, contracts.PHONE_BILL_RESPONSE)
async def get(params):
    """Get phone bill."""
    LOGGER.debug("Received phone bill get request")
    service = services.build_phone_bill()
    return service.list(params.phone_number,
                        params.period,
                        params.page,
                        params.limit)
