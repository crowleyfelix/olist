def call_record_start():
    return {
        "type": "start",
        "timestamp": 1456758001.0,
        "call_id": 70,
        "source": "99988526423",
        "destination": "9993468278"
    }


def call_record_end():
    return {
        "type": "end",
        "timestamp": 1456758001.0,
        "call_id": 70,
    }
