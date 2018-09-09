"""Module with billing processors."""
from app.utils import datetime
from app.models.enums import ChargeStrategy

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


def process(calls, period, charge_strategy=ChargeStrategy.homogeneous):
    """Process calls."""
    bill = []
    for call in calls:

        start_date = datetime.from_timestamp(call["start_timestamp"])
        end_date = datetime.from_timestamp(call["end_timestamp"])
        call["price"] = calculate_price(start_date, end_date, charge_strategy)
        call["period"] = period

        bill.append(call)

    return bill


def calculate_price(start_date, end_date, charge_strategy):
    """Process call price."""
    if charge_strategy is ChargeStrategy.homogeneous:
        return _calculate_homogeneous_price(start_date, end_date)
    elif charge_strategy is ChargeStrategy.heterogeneous:
        return _calculate_heterogeneous_price(start_date, end_date)
    else:
        raise TypeError("Invalid charge strategy passed")


def _calculate_heterogeneous_price(start_date, end_date):
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


def _calculate_homogeneous_price(start_date, end_date):
    amount = DEFAULT_FIXED_CHARGE

    for charge in CALL_CHARGES:
        if datetime.is_between_time(start_date,
                                    charge["start"],
                                    charge["end"]):

            delta = end_date - start_date
            minutes = int(delta.total_seconds() / 60)

            amount += charge["value"] * minutes
            break

    return amount
