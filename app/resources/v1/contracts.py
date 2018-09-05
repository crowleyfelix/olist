"""Module with data schemas."""
from app.models import enums
from app.utils import datetime
from glom import Coalesce, OMIT, Call, T

DEFAULT_PAGE = 1
DEFAULT_LIMIT = 10

CALL_RECORD_REQUEST = {
    "body": {
        "type": ("type", enums.CallRecordType),
        "timestamp": ("timestamp", float),
        "call_id": ("call_id", int),
        "source": Coalesce("source", str, default=OMIT),
        "destination": Coalesce("destination", str, default=OMIT)
    }
}

CALL_RECORD_RESPONSE = {
    "id": Coalesce("id", default="todo"),
    "type": "type",
    "timestamp": "timestamp",
    "call_id": ("call_id", int),
    "source": Coalesce("source", default=OMIT),
    "destination": Coalesce("destination", default=OMIT)
}

PHONE_BILL_REQUEST = {
    "params": {
        "phone_number": "phone_number",
        "period": (Coalesce("period", default='')),
        "page": (Coalesce("page", default=DEFAULT_PAGE), int),
        "limit": (Coalesce("limit", default=DEFAULT_LIMIT), int)
    }
}

PHONE_BILL_RESPONSE = [{
    "start_date": ("start_timestamp", datetime.to_date_str),
    "start_time": ("start_timestamp", datetime.to_time_str),
    "duration":   Call(datetime.diff_str,
                       args=[T["end_timestamp"], T["start_timestamp"]]),
    "destination": "destination",
    "price": ("price", lambda p: p/100),
}]
