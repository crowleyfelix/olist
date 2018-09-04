"""Module with data schemas."""
from app.models import enums
from glom import Coalesce

DEFAULT_PAGE = 1
DEFAULT_LIMIT = 10

CALL_RECORD_REQUEST = {
    "body": {
        "type": ("type", enums.CallRecordType),
        "timestamp": ("timestamp", float),
        "call_id": ("call_id", int),
        "source": ("source", str),
        "destination": ("destination", str)
    }
}

CALL_RECORD_RESPONSE = {
    **CALL_RECORD_REQUEST["body"],
    "id": Coalesce("id", default="todo"),
    "type": "type"
}

PHONE_BILL_REQUEST = {
    "params": {
        "phone_number": "phone_number",
        "period": (Coalesce("page", default='')),
        "page": (Coalesce("page", default=DEFAULT_PAGE), int),
        "limit": (Coalesce("limit", default=DEFAULT_LIMIT), int)
    }
}
