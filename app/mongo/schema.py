"""Module with data schemas."""
from glom import glom, Check
from app.models import enums
from app.processors import validation

CALL_RECORD = {
    "type": ("type.value", Check(validate=lambda x: enums.CallRecordType(x))),
    "timestamp": ("timestamp", Check(type=float)),
    "call_id": ("call_id", Check(type=int)),
    "source": ("source", Check(type=str, validate=validation.phone_number)),
    "destination": ("destination", Check(type=str,
                                         validate=validation.phone_number))
}


def validate(data, schema):
    """Validate data."""
    return glom(data, schema)
