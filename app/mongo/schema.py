"""Module with data schemas."""
from glom import glom, Check, OMIT
from app.models import enums
from app.processors import validation


def validate_phone_number(text):
    if text:
        return validation.phone_number(text)

    return True


CALL_RECORD = {
    "type": ("type.value",
             Check(validate=lambda x: enums.CallRecordType(x))),
    "timestamp": ("timestamp",
                  Check(type=float)),
    "call_id": ("call_id",
                Check(type=int)),
    "source": ("source",
               Check(type=str,
                     default=OMIT,
                     validate=validate_phone_number)),
    "destination": ("destination",
                    Check(type=str,
                          default=OMIT,
                          validate=validate_phone_number))
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
