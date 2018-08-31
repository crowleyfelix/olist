"""Module with datetime processors."""
from datetime import timedelta


def get_cycle_ocurrencies(start_range, end_range,
                          start_cycle, end_cycle):
    """Get cycle ocurrencies from date range ."""
    ocurrencies = []

    started_cycle = start_range

    while started_cycle < end_range:

        if start_cycle <= started_cycle.time() <= end_cycle:

            if end_cycle < end_range.time():
                ended_cycle = to_next_time(started_cycle, end_cycle)
            else:
                ended_cycle = end_range

            ocurrencies.append((started_cycle, ended_cycle))

        started_cycle = to_next_time(started_cycle, start_cycle)

    return ocurrencies


def to_next_time(datetime, time):
    days_to_add = 0

    if datetime.time() >= time:
        days_to_add = 1

    datetime += timedelta(days=days_to_add)
    return datetime.replace(hour=time.hour,
                            minute=time.minute,
                            second=time.second)
