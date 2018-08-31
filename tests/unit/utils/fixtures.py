from datetime import datetime

parse = datetime.strptime

dtfmt = "%Y-%m-%dT%H:%M:%SZ"
tfmt = "%H:%M"

START_RANGE = parse("2018-02-28T21:57:13Z", dtfmt)
END_RANGE = parse("2018-03-01T22:10:56Z", dtfmt)

STANDARD_CYCLE = {
    "start": parse("06:00", tfmt).time(),
    "end": parse("22:00", tfmt).time(),
    "ocurrencies": [
        (parse("2018-02-28T21:57:13Z", dtfmt),
         parse("2018-02-28T22:00:00Z", dtfmt)),
        (parse("2018-03-01T06:00:00Z", dtfmt),
         parse("2018-03-01T22:00:00Z", dtfmt))
    ]
}

REDUCED_CYCLE = {
    "start": parse("22:00", tfmt).time(),
    "end": parse("06:00", tfmt).time(),
    "ocurrencies": [
        (parse("2018-02-28T22:00:00Z", dtfmt),
         parse("2018-03-01T06:00:00Z", dtfmt)),
        (parse("2018-03-01T22:00:00Z", dtfmt),
         parse("2018-03-01T22:10:56Z", dtfmt))
    ]
}
