"""Errors raised by the client, independently of Socket.IO internals."""


class WomError(Exception):
    """Base class for client errors."""


class AuthorizationError(WomError):
    """Authorization was rejected, malformed, or revoked."""


class ConnectionError(WomError):
    """A shard could not connect or disconnected with requests outstanding."""


class RequestTimeout(WomError, TimeoutError):
    """A request exceeded its total deadline, including connection and pacing."""


class ProtocolError(WomError):
    """The server sent a malformed frame or explicitly skipped a request."""


class ServerError(WomError):
    """The server reported an error event."""


class ServerRequired(WomError, ValueError):
    """A game API requires the game's server to be supplied explicitly."""


class ClientClosed(WomError):
    """The client has been closed and cannot be reused."""


class EventOverflow(WomError):
    """A subscription exceeded its bounded buffer; no loss is silently hidden."""
