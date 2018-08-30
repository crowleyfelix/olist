"""Module that contains call record resources."""
from app import services
from app.infrastructure import web


def register(blueprint):
    """Register call records namespace."""
    blueprint.add_route(create, "/call-records", methods=['POST'])


async def create(request):
    """Create call reco[d."""
    service = services.CallRecord()

    body = request.json

    record = service.create(body)
    return web.json(record)
