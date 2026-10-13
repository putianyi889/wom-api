"""Unofficial Minesweeper Online data client."""

from .catalog import APIS, EVENT_NAMES, PROTOCOL_VERSION, ApiSpec
from .client import WomClient
from .events import EventStream
from .exceptions import (
    AuthorizationError,
    ClientClosed,
    ConnectionError,
    EventOverflow,
    ProtocolError,
    RequestTimeout,
    ServerError,
    ServerRequired,
    WomError,
)
from .types import Authorization, Event, JsonValue, Payload

__version__ = "0.1.0"

__all__ = [
    "APIS",
    "EVENT_NAMES",
    "PROTOCOL_VERSION",
    "ApiSpec",
    "Authorization",
    "AuthorizationError",
    "ClientClosed",
    "ConnectionError",
    "Event",
    "EventOverflow",
    "EventStream",
    "JsonValue",
    "Payload",
    "ProtocolError",
    "RequestTimeout",
    "ServerError",
    "ServerRequired",
    "WomClient",
    "WomError",
    "__version__",
]
