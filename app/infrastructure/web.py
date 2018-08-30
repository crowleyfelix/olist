"""Module with web web service engine."""
# pylama:ignore=W0611
from sanic import Sanic as Engine
from sanic import exceptions
from sanic.response import json
from sanic.blueprints import Blueprint
