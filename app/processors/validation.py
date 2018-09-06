"""Module with validators."""
from app.utils import datetime


def phone_number(text):
    """Validate phone number."""
    text = str(text)
    return text.isnumeric() and (10 <= len(text) <= 11)


def year_month(period):
    """Validate year month format."""
    try:
        datetime.to_datetime(period, datetime.YEAR_MONTH_FMT)
        return True
    except ValueError:
        return False
