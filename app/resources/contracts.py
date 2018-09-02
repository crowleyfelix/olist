"""Module with default API contracts."""


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
