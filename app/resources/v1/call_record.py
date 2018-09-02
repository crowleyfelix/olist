"""Module that contains call record resources."""
from app import services
from app.infrastructure import web
from .contracts import build_response


def register(blueprint):
    """Register call records namespace."""
    blueprint.add_route(create, "/call-records", methods=['POST'])


async def create(request):
    """Create call record."""
    service = services.CallRecord()

    call_record = _validate(request)

    call_record = service.create(call_record)
    return web.json(build_response(call_record))


def _validate(request):
    return request.json
