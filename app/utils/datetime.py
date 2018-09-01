"""Module with datetime processors."""
import pandas
from datetime import timedelta


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
