"""Module with mongo handlers."""
import pymongo
from app.infrastructure import get_config


def get_collection(name):
    """Get mongo collection."""
    config = get_config()
    mongo_config = config.mongo

    conn = pymongo.MongoClient(mongo_config.uri)
    database = conn[mongo_config.database]
    return database[name]
