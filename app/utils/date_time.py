"""Module with datetime processors."""
from datetime import timedelta


class DateTimeCycle(object):
    """Class to handle with datetime cycles."""

    @classmethod
    def get_cycle_ocurrencies(cls, start_range, end_range,
                              start_cycle, end_cycle):
        """Get cycle ocurrencies from date range ."""
        ocurrencies = []

        started_cycle, ended_cycle = cls.find_current_cycle(
            start_range, start_cycle, end_cycle)

        while start_range < end_range:

            # If start range is between cycle, append ocurrencies
            if is_in_range(start_range, started_cycle, ended_cycle):
                if ended_cycle < end_range:
                    ocurrencies.append((start_range, ended_cycle))
                else:
                    ocurrencies.append((start_range, end_range))

            start_range = to_next_time(start_range, start_cycle)

            # If start range is greater then start cycle, go to next cycle
            if start_range > started_cycle:
                started_cycle, ended_cycle = cls.get_next_cycle(
                    started_cycle, ended_cycle)

        return ocurrencies

    @staticmethod
    def find_current_cycle(reference_datetime, start_cycle, end_cycle):
        """Find current cycle from date reference."""
        if is_in_range(reference_datetime.time(), start_cycle, end_cycle):
            started_cycle = to_previous_time(reference_datetime, start_cycle)
        else:
            started_cycle = to_next_time(reference_datetime, start_cycle)

        ended_cycle = to_next_time(started_cycle, end_cycle)

        return (started_cycle, ended_cycle)

    @staticmethod
    def get_next_cycle(started_cycle, ended_cycle):
        """Get to next cycle."""
        started_cycle = to_next_time(started_cycle, started_cycle.time())
        ended_cycle = to_next_time(ended_cycle, ended_cycle.time())

        return (started_cycle, ended_cycle)


def is_in_range(reference, start_range, end_range):
    """Is reference in range."""
    return start_range <= reference <= end_range


def to_previous_time(datetime, time):
    """Get to previous time."""
    days_to_add = 0

    if datetime.time() <= time:
        days_to_add = 1

    datetime -= timedelta(days=days_to_add)
    return datetime.replace(hour=time.hour,
                            minute=time.minute,
                            second=time.second)


def to_next_time(datetime, time):
    """Get to next time."""
    days_to_add = 0

    if datetime.time() >= time:
        days_to_add = 1

    datetime += timedelta(days=days_to_add)
    return datetime.replace(hour=time.hour,
                            minute=time.minute,
                            second=time.second)
