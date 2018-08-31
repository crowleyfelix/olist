"""Module with datetime processors."""
import pandas

PANDAS_MIN_FREQUENCY = "min"


def get_cycle_ocurrencies(cls, start_range, end_range,
                          start_cycle, end_cycle):
    """Get cycle ocurrencies from date range ."""
    ocurrencies = []

    range_datetime = pandas.date_range(start_range,
                                       end_range,
                                       freq=PANDAS_MIN_FREQUENCY)

    serie = range_datetime.to_series()
    filtered = serie.between_time(start_cycle, end_cycle)

    started_cycle = None
    for item in filtered:

        if not started_cycle:
            started_cycle = item

        if item.time() == end_cycle:
            ocurrencies.append((started_cycle, item))
            started_cycle = None

    return ocurrencies
