"""Module with validators."""
from app.utils import datetime


def phone_number(text):
    """Validate phone number."""
    text = str(text)
    return text.isnumeric() and (10 <= len(text) <= 11)


def period_format(period):
    """Validate year month format."""
    try:
        datetime.to_datetime(period, datetime.YEAR_MONTH_FMT)
        return True
    except ValueError:
        return False


def closed_bill_period(period):
    """Validate if period could have closed bill."""
    date = datetime.to_datetime(period, datetime.YEAR_MONTH_FMT)
    today = datetime.today()

    if date.year <= today.year:
        return True

    if date.month < today.month:
        return True

    return False
