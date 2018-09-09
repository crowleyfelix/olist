"""Module with billing processors."""
from app.utils import datetime

DEFAULT_FIXED_CHARGE = 36

CALL_CHARGES = [
    {
        "value": 9,
        "start": datetime.to_time("6:00"),
        "end": datetime.to_time("22:00")
    },
    {
        "value": 0,
        "start": datetime.to_time("22:00"),
        "end": datetime.to_time("06:00")
    }
]


def process(calls, period):
    """Process calls."""
    bill = []
    for call in calls:

        start_date = datetime.from_timestamp(call["start_timestamp"])
        end_date = datetime.from_timestamp(call["end_timestamp"])
        call["price"] = calculate_price(start_date, end_date)
        call["period"] = period

        bill.append(call)

    return bill


def calculate_price(start_date, end_date):
    """Process call price."""
    amount = DEFAULT_FIXED_CHARGE

    for charge in CALL_CHARGES:
        cycles = datetime.get_cycle_ocurrencies(start_date,
                                                end_date,
                                                charge["start"],
                                                charge["end"])

        for start_cycle, end_cycle in cycles:
            delta = end_cycle - start_cycle
            minutes = int(delta.total_seconds() / 60)

            amount += charge["value"] * minutes

    return amount
