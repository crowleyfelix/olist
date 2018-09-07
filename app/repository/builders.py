"""Module with repository builders."""
from .call_record import CallRecord
from .call import Call
from .phone_bill import PhoneBill
from . import constants, mongo


def build_call_record():
    """Build call record repository."""
    collection = mongo.get_collection(constants.CALL_RECORD_COLLECTION)
    return CallRecord(collection)


def build_call():
    """Build call record repository."""
    collection = mongo.get_collection(constants.CALL_RECORD_COLLECTION)
    return Call(collection)


def build_phone_bill():
    """Build phone bill repository."""
    collection = mongo.get_collection(constants.PHONE_BILL_COLLECTION)
    return PhoneBill(collection)
