"""Module with mongo handlers."""
import pymongo
from app.infrastructure import get_config
from app.infrastructure.configuration import AppMode

TEST_DB = "test"
_COLLECTIONS = {}


def get_collection(name):
    """Get mongo collection."""
    if not _COLLECTIONS.get(name):
        config = get_config()
        mongo_config = config.mongo

        database = mongo_config.database
        if config.mode == AppMode.TEST:
            database = TEST_DB

        conn = pymongo.MongoClient(mongo_config.uri)
        database = conn[database]
        _COLLECTIONS[name] = database[name]

    return _COLLECTIONS[name]


def is_ok():
    """Verify if mongo is ok."""
    config = get_config()
    mongo_config = config.mongo
    database = mongo_config.database
    conn = pymongo.MongoClient(mongo_config.uri)
    database = conn[database]

    try:
        database.command("ping")
        return True
    except Exception:
        return False
