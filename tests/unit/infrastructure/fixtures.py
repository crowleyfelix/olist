from munch import munchify
from app.infrastructure.configuration import AppMode


def config():
    return munchify({
        "host": "host",
        "port": "port",
        "mode": AppMode.DEBUG,
        "logging": {
            "config": "CONFIG",
        }
    })
