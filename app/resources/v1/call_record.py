"""Module that contains call record resources."""
import logging
from app import services
from app.resources.contracts import auto_parse
from . import contracts

LOGGER = logging.getLogger(__name__)


def register(blueprint):
    """Register call records namespace."""
    blueprint.add_route(post, "/call-records", methods=['POST'])


@auto_parse(contracts.CALL_RECORD_REQUEST,
            contracts.CALL_RECORD_RESPONSE,
            status=201)
async def post(body):
    """Create call record."""
    LOGGER.debug("Received call record post request")
    service = services.build_call_record()
    return service.create(body)
