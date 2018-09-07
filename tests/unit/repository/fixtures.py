from munch import munchify
from app.infrastructure.configuration import AppMode


def config():
    return munchify({
        "mode": AppMode.TEST,
        "mongo": {
            "uri": "CONFIG",
            "database": "database",
        }
    })
