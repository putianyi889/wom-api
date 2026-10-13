"""Discoverable catalogue of the current public browser API classes."""

from __future__ import annotations

import json
from dataclasses import dataclass
from importlib.resources import files
from types import MappingProxyType
from typing import Any


@dataclass(frozen=True)
class ApiSpec:
    """An observed controller; field observations are not a server schema."""

    controller: str
    method: str
    role: str
    skip_rate_limit: bool
    limited_functionality: bool
    closes_session: bool
    request_fields: tuple[tuple[str, ...], ...]
    response_fields: tuple[str, ...]
    table_query_fields: tuple[tuple[str, ...], ...]
    table_sorts: tuple[str, ...]


_catalog: dict[str, Any] = json.loads(files(__package__).joinpath("api_catalog.json").read_text())
PROTOCOL_VERSION: int = _catalog["version"]
SOURCE_URL: str = _catalog["source_url"]
SOURCE_SHA256: str = _catalog["sha256"]
EVENT_NAMES: tuple[str, ...] = tuple(_catalog["events"])
APIS = MappingProxyType(
    {
        a["controller"]: ApiSpec(
            a["controller"],
            a["method"],
            a["role"],
            a["skip_rate_limit"],
            a["limited_functionality"],
            a["closes_session"],
            tuple(tuple(s["fields"]) for s in a["observed_requests"]),
            tuple(a["observed_response_fields"]),
            tuple(tuple(shape) for shape in a["table_query_fields"]),
            tuple(a["table_sorts"]),
        )
        for a in _catalog["apis"]
    }
)
