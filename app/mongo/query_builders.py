"""Module with mongo query builders."""


def CallRecord(object):
    """Query builder for call record operations."""
    @staticmethod
    def by_billing_cycle(phone_number, start_timestamp, end_timestamp):
        return {
            "source": phone_number,
        }
