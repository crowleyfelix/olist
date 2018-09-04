"""Module with default API contracts."""
from glom import glom
from functools import wraps
from app.infrastructure import web
from sanic.exceptions import InvalidUsage
from munch import munchify


def auto_parse(request_schema,
               response_schema):
    """Auto parse calls."""
    def wrapper(func):
        @wraps(func)
        async def wrapped(request, *args, **kwargs):
            parsed = {}

            body_schema = request_schema.get("body")
            params_schema = request_schema.get("params")

            if body_schema:
                try:
                    body = request.json
                    parsed["body"] = glom(body, body_schema)
                except ValueError:
                    raise InvalidUsage("Invalid body sent.")

            if params_schema:
                try:
                    params = {**request.raw_args,  **kwargs}
                    parsed["params"] = munchify(glom(params, params_schema))
                except (ValueError, KeyError):
                    raise InvalidUsage("Invalid params sent.")

            result = await func(**parsed)
            data, page_info = None

            if isinstance(result, tuple):
                data, page_info = result
            else:
                data = result

            data = glom(data, response_schema)

            response = build_response(data, page_info)
            return web.json(response)

        return wrapped
    return wrapper


def build_response(data=None, page_info=None, messages=None):
    """Build api response."""
    if data is None:
        data = {}

    if messages is None:
        messages = []

    response = {
        "data": data,
        "messages": messages,
    }
    if page_info:
        response.update(**page_info)

    return response
