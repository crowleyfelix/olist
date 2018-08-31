"""Module with datetime processors."""
from datetime import timedelta


def get_cycle_ocurrencies(start_range, end_range,
                          start_cycle, end_cycle):
    """Get cycle ocurrencies from date range ."""
    ocurrencies = []

    start_cycle = to_closer_time(start_range, start_cycle)
    end_cycle = to_next_time(start_range, end_cycle)

    import pdb
    pdb.set_trace()
    while start_range < end_range:

        # If start range is between cycle, append ocurrencies
        if start_cycle <= start_range <= end_cycle:

            if end_cycle < end_range:
                ocurrencies.append((start_range, end_cycle))
            else:
                ocurrencies.append((start_range, end_range))

        start_range = to_next_time(start_range, start_cycle.time())

        # If start range is greater then start cycle, go to next cycle
        if start_range > start_cycle:
            start_cycle = to_next_time(start_cycle, start_cycle.time())
            end_cycle = to_next_time(end_cycle, end_cycle.time())

    return ocurrencies


def to_closer_time(datetime, time):
    """Go to closer time."""
    previous_time = to_previous_time(datetime, time)
    next_time = to_next_time(datetime, time)

    diff_previous = datetime - previous_time
    diff_next = next_time - datetime

    if diff_previous <= diff_next:
        return previous_time

    return next_time


def to_previous_time(datetime, time):
    """Go to previous time."""
    days_to_add = 0

    if datetime.time() < time:
        days_to_add = 1

    datetime -= timedelta(days=days_to_add)
    return datetime.replace(hour=time.hour,
                            minute=time.minute,
                            second=time.second)


def to_next_time(datetime, time):
    """Go to next time."""
    days_to_add = 0

    if datetime.time() >= time:
        days_to_add = 1

    datetime += timedelta(days=days_to_add)
    return datetime.replace(hour=time.hour,
                            minute=time.minute,
                            second=time.second)
