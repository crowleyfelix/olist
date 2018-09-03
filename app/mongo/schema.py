"""Module with data schemas."""
from glom import Check

CALL_RECORD = {
    "type": ("type", Check(type=str, one_of=["start", "end"])),
    "timestamp": ("timestamp", Check(type=float)),
    "call_id": ("call_id", Check(type=int)),
    "source": ("source", Check(type=str)),
    "destination": ("destination", Check(type=str))
}
