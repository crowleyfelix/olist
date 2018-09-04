"""Module with data schemas."""
from glom import Check
from app.models import enums
from app.processors import validation

CALL_RECORD = {
    "type": ("type", Check(type=enums.CallRecordType)),
    "timestamp": ("timestamp", Check(type=float)),
    "call_id": ("call_id", Check(type=int)),
    "source": ("source", Check(type=str, validate=validation.phone_number)),
    "destination": ("destination", Check(type=str,
                                         validate=validation.phone_number))
}
