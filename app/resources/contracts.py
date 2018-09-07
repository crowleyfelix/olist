"""Module with default API contracts."""
from functools import wraps
from glom import glom, GlomError
from munch import munchify
from app import errors
from app.infrastructure import web


def auto_parse(request_schema,
               response_schema,
               status=200):
    """Auto parse calls."""
    def wrapper(func):
        @wraps(func)
        async def wrapped(request, *args, **kwargs):
            parsed = {}

            body_schema = request_schema.get("body")
            params_schema = request_schema.get("params")

            try:
                if body_schema:
                    body = request.json
                    parsed["body"] = glom(body, body_schema)

                if params_schema:
                    params = {**request.raw_args,  **kwargs}
                    parsed["params"] = munchify(glom(params, params_schema))

            except (ValueError, KeyError):
                raise errors.SchemaError()
            except GlomError as ex:
                raise errors.SchemaError(glom_error=ex)

            result = await func(**parsed)
            data = None
            page_info = None

            if isinstance(result, tuple):
                data, page_info = result

                if not page_info["size"]:
                    errors.NotFoundError()
            else:
                data = result

            data = glom(data, response_schema)

            response = build_response(data, page_info)
            return web.json(response, status)

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
