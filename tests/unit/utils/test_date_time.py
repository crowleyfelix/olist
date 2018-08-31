from datetime import datetime
from unittest import TestCase
from app.utils.date_time import get_cycle_ocurrencies

fmt = "%Y-%m-%dT%H:%M:%SZ"
start_range = datetime.strptime("2018-02-28T21:57:13Z", fmt)
end_range = datetime.strptime("2018-03-01T22:10:56Z", fmt)

start_cycle = datetime.strptime("06:00", "%H:%M").time()
end_cycle = datetime.strptime("22:00", "%H:%M").time()

start_cycle = datetime.strptime("22:00", "%H:%M").time()
end_cycle = datetime.strptime("06:00", "%H:%M").time()

# Standard
standard_ocurrencies = [
    ("2018-02-28T21:57:13Z", "2018-02-28T22:00:00Z"),
    ("2018-03-01T06:00:00Z", "2018-03-01T22:22:00Z")
]

# Reduced
reduced_ocurrencies = [
    ("2018-02-28T22:00:00Z", "2018-03-01T06:00:00Z"),
    ("2018-03-01T22:22:00Z", "2018-03-01T22:10:56Z")
]


class TestDateTime(TestCase):
    def test_get_cycle_ocurrencies(self):
        ocurrencies = get_cycle_ocurrencies(
            start_range, end_range, start_cycle, end_cycle)

        import pdb
        pdb.set_trace()
