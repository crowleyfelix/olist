"""Module with mongo query builders."""
import json
import pystache
from os import path
from app.infrastructure.configuration import get_config


LIST_CALLS = "list-calls.query"

_QUERIES = {}


def build(query_name, **kwargs):
    """Build query for searching call records at billing cyle."""
    query = _QUERIES.get(query_name)

    if not query:
        config = get_config()

        with open(path.join(config.queries_path, query_name)) as f:
            query = f.read()

        _QUERIES[query_name] = query

    return json.loads(pystache.render(query, kwargs))
