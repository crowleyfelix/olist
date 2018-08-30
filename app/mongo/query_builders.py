"""Module with mongo query builders."""


class CallRecord(object):
    """Query builder for call record operations."""

    @staticmethod
    def by_billing_cycle(phone_number, start_timestamp, end_timestamp):
        """Build query for searching call records at billing cyle."""
        return {
            "source": phone_number,
        }
