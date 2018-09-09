def call_record_start():
    return {
        "type": "start",
        "timestamp": 1519865833.0,
        "call_id": 70,
        "source": "99988526423",
        "destination": "9993468278"
    }


def call_record_end():
    return {
        "type": "end",
        "timestamp": 1519953056.0,
        "call_id": 70,
    }


def phone_bill():
    return {
        "start_date": "2018-02-28",
        "start_time": "21:57",
        "duration": "24h13m43s",
        "destination": "9993468278",
        "price": 131.13
    }
