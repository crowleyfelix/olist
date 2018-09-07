def call_record_start():
    return {
        "type": "start",
        "timestamp": 123.0,
        "call_id": 1,
        "source": "1234567890",
        "destination": "123456789"
    }


def call_record_end():
    return {
        "type": "end",
        "timestamp": 123.0,
        "call_id": 1,
    }


def call():
    return {
        "call_id": 1
        "start_timestamp": 123.0
        "end_timestamp": 123.0
        "source": "1234567890",
        "destination": "123456789",
    }
