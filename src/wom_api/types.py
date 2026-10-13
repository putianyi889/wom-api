"""Public protocol types. Responses retain the site's original JSON field names."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeAlias

JsonValue: TypeAlias = None | bool | int | float | str | list["JsonValue"] | dict[str, "JsonValue"]
Payload: TypeAlias = dict[str, JsonValue]


@dataclass(frozen=True)
class Authorization:
    """Authorization returned by HTTP bootstrap; secrets are omitted from repr."""

    user_id: int
    session_id: int
    session: str = field(repr=False)
    ticket: str = field(repr=False)
    ticket_expires_at: int
    user: Payload = field(repr=False)


@dataclass(frozen=True)
class Event:
    """A server push, with the original argument list and source shard."""

    name: str
    params: list[JsonValue]
    server: str
    request_id: int = 0
