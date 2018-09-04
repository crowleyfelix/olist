"""Module that contains call record resources."""
from app import services
from app.resources.contracts import auto_parse
from . import contracts


def register(blueprint):
    """Register call records namespace."""
    blueprint.add_route(create, "/call-records", methods=['POST'])


@auto_parse(contracts.CALL_RECORD_REQUEST,
            contracts.CALL_RECORD_RESPONSE)
async def create(body):
    """Create call record."""
    service = services.CallRecord()
    return service.create(body)
