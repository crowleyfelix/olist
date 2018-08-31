"""Module with billing processors."""
DEFAULT_FIXED_CHARGE = 0.36

CALL_CHARGES = [
    {
        "value": 0.09,
        "start_time": "6:00",
        "end_time": "22:00"
    },
    {
        "value": 0,
        "start_time": "22:00",
        "end_time": "06:00"
    }
]
