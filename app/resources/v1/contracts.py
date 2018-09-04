"""Module with data schemas."""
from app.models import enums
from app.services.phone_bill import DEFAULT_PAGE, DEFAULT_LIMIT
from glom import Coalesce

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
    "id": ("id", int),
    **CALL_RECORD_REQUEST
}

PHONE_BILL_REQUEST = {
    "params": {
        "phone_number": "phone_number",
        "period": "period",
        "page": (Coalesce("page", default=DEFAULT_PAGE), int),
        "limit": (Coalesce("limit", default=DEFAULT_LIMIT), int)
    }
}
