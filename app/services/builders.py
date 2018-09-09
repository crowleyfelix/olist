"""Module with service builders."""
from .call_record import CallRecord
from .phone_bill import PhoneBill


def build_call_record():
    """Build call record service."""
    return CallRecord()


def build_phone_bill():
    """Build phone bill service."""
    return PhoneBill()
