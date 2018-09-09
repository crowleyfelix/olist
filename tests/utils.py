from datetime import datetime

parse = datetime.strptime

dtfmt = "%Y-%m-%dT%H:%M:%SZ"
tfmt = "%H:%M"


def parse_time(raw):
    return datetime.strptime(raw, tfmt).time()


def parse_datetime(raw):
    return datetime.strptime(raw, dtfmt)
