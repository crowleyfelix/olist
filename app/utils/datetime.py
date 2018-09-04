"""Module with datetime processors."""
import pandas
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

DATETIME_FMT = "%Y-%m-%dT%H:%M:%SZ"
TIME_FMT = "%H:%M"
YEAR_MONTH_FMT = "%Y-%m"


def date_range(start, end):
    """Create date range."""
    cursor = start

    while cursor < end:
        yield cursor
        cursor += timedelta(minutes=1, seconds=-cursor.second)

    yield end


def get_cycle_ocurrencies(start_range, end_range,
                          start_cycle, end_cycle):
    """Get cycle ocurrencies from date range ."""
    ocurrencies = []

    range_datetime = date_range(start_range, end_range)
    idx = pandas.to_datetime(list(range_datetime))
    serie = idx.to_series()

    filtered = serie.between_time(start_cycle, end_cycle)

    started_cycle = None
    for item in filtered:

        if not started_cycle:
            started_cycle = item.to_pydatetime()

        elif item.time() == end_cycle or item == filtered[-1]:
            ended_cycle = item.to_pydatetime()
            ocurrencies.append((started_cycle, ended_cycle))

            started_cycle = None

    return ocurrencies


def to_time(raw):
    """Convert to time."""
    return datetime.strptime(raw, TIME_FMT).time()


def to_datetime(raw, fmt=DATETIME_FMT):
    """Convert to datetime."""
    return datetime.strptime(raw, fmt)


def begin_end_month(period):
    """Get begin day and end day month from period."""
    begin = to_datetime(period, YEAR_MONTH_FMT)
    end = begin + relativedelta(months=1, seconds=-1)
    return (begin, end)


def begin_end_previous_month():
    """Get begin day and end day month from previous month."""
    reference_date = datetime.today() - relativedelta(month=1)

    period = f"{reference_date.year}{reference_date.month}"
    return begin_end_month(period)


def from_timestamp(timestamp):
    """Convert timestamp to datetime."""
    return datetime.fromtimestamp(timestamp)
