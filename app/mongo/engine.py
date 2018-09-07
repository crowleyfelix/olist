"""Module with mongo handlers."""
import pymongo
from app.infrastructure import get_config

_COLLECTIONS = {}


def get_collection(name):
    """Get mongo collection."""
    if not _COLLECTIONS.get(name):
        config = get_config()
        mongo_config = config.mongo

        conn = pymongo.MongoClient(mongo_config.uri)
        database = conn[mongo_config.database]
        _COLLECTIONS[name] = database[name]

    return _COLLECTIONS[name]
