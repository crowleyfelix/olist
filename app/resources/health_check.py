"""Module that exposes health check resources functions."""

from app.infrastructure import web


def register(engine):
    """Register health check routes."""
    engine.add_route(health_check, "/health-check")


async def health_check(request):
    """Start health check resource controller."""
    return web.json({"messages":
                     ["Hi! I'm alive and well. Thanks for caring"]})
