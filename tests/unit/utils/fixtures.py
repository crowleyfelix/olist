from tests.utils import parse_time, parse_datetime

START_RANGE = parse_datetime("2018-02-28T21:57:13Z")
END_RANGE = parse_datetime("2018-03-01T22:10:56Z")

STANDARD_CYCLE = {
    "start": parse_time("06:00"),
    "end": parse_time("22:00"),
    "ocurrencies": [
        (parse_datetime("2018-02-28T21:57:13Z"),
         parse_datetime("2018-02-28T22:00:00Z")),
        (parse_datetime("2018-03-01T06:00:00Z"),
         parse_datetime("2018-03-01T22:00:00Z"))
    ]
}

REDUCED_CYCLE = {
    "start": parse_time("22:00"),
    "end": parse_time("06:00"),
    "ocurrencies": [
        (parse_datetime("2018-02-28T22:00:00Z"),
         parse_datetime("2018-03-01T06:00:00Z")),
        (parse_datetime("2018-03-01T22:00:00Z"),
         parse_datetime("2018-03-01T22:10:56Z"))
    ]
}
