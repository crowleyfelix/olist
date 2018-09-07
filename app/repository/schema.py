"""Module with data schemas."""
from glom import glom, Check, GlomError, Coalesce, OMIT
from app.models import enums
from app.processors import validation
from app.errors import SchemaError


def parse_id(t):
    """Parse mongo id."""
    return str(t) if t is not OMIT else OMIT


CALL_RECORD_START = {
    "id": (Coalesce("_id", default=OMIT), parse_id),
    "type": (Coalesce("type.value", "type"),
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
    "id": (Coalesce("_id", default=OMIT), parse_id),
    "type": (Coalesce("type.value", "type"),
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


CALL = {
    "call_id": ("_id",
                Check(type=int)),
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
}

PHONE_BILL = {
    "id": (Coalesce("_id", default=OMIT), parse_id),
    "call_id": ("call_id",
                Check(type=int)),
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
                     validate=validation.period_format))
}


def parse(data, schema):
    """Parse data."""
    try:
        return glom(data, schema)
    except (ValueError, KeyError):
        raise SchemaError()
    except GlomError as ex:
        raise SchemaError(glom_error=ex)
