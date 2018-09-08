"""Module that exposes health check resources functions."""

from app.infrastructure import web
from app.repository import mongo
from app.resources.contracts import build_response

_DEPENDENCIES = {
    "mongo": mongo.is_ok
}


def register(engine):
    """Register health check routes."""
    engine.add_route(health_check, "/")


async def health_check(request):
    """Start health check resource controller."""
    dependencies = _get_dependencies()

    if any(d == "failed" for _, d in dependencies.items()):
        message = "Hi. I'm not so good. But, thanks for caring"
        status = 500
    else:
        message = "Hi! I'm alive and well. Thanks for caring"
        status = 200

    return web.json(build_response(dependencies, messages=[message]),
                    status)


def _get_dependencies():
    dependencies = {}

    for name, dep in _DEPENDENCIES.items():
        dependencies[name] = "ok" if dep() else "failed"

    return dependencies
