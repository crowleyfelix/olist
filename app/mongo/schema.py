"""Module with data schemas."""
from glom import glom, Check
from app.models import enums
from app.processors import validation


CALL_RECORD_START = {
    "type": ("type.value",
             Check(validate=lambda x: enums.CallRecordType(x))),
    "timestamp": ("timestamp",
                  Check(type=float)),
    "call_id": ("call_id",
                Check(type=int)),
    "source": ("source",
               Check(type=str,
                     validate=validation.phone_number)),
    "destination": ("destination",
                    Check(type=str,
                          validate=validation.phone_number))
}

CALL_RECORD_END = {
    "type": ("type.value",
             Check(validate=lambda x: enums.CallRecordType(x))),
    "timestamp": ("timestamp",
                  Check(type=float)),
    "call_id": ("call_id",
                Check(type=int)),
}

CALL_RECORD = {
    enums.CallRecordType.start: CALL_RECORD_START,
    enums.CallRecordType.end: CALL_RECORD_END
}


PHONE_BILL = {
    "start_timestamp": ("start_timestamp",
                        Check(type=float)),
    "end_timestamp": ("end_timestamp",
                      Check(type=float)),
    "source": ("source",
               Check(type=str,
                     validate=validation.phone_number)),
    "destination": ("destination",
                    Check(type=str,
                          validate=validation.phone_number)),
    "price": ("price", int),
    "period": ("period",
               Check(type=str,
                     validate=validation.year_month))
}


def validate(data, schema):
    """Validate data."""
    return glom(data, schema)
