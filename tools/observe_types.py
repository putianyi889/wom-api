"""Explicitly collect public API type observations; store schemas, not values.

Requires an installed wom-api checkout and the research extra. Nothing is
collected on import, build, CI, or ordinary catalogue generation.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import ssl
from datetime import UTC, datetime
from pathlib import Path

from genson import SchemaBuilder

from wom_api import PROTOCOL_VERSION, WomClient
from wom_api.catalog import SOURCE_SHA256


def omit_required(schema: dict) -> dict:
    """Sample presence is not a required-field contract."""
    result = {key: value for key, value in schema.items() if key != "required"}
    # A property named "required" is data, not the schema's required keyword.
    if "properties" in result:
        result["properties"] = {
            name: omit_required(child) for name, child in result["properties"].items()
        }
    if isinstance(result.get("items"), dict):
        result["items"] = omit_required(result["items"])
    for keyword in ("anyOf", "allOf", "oneOf"):
        if keyword in result:
            result[keyword] = [omit_required(child) for child in result[keyword]]
    return result


async def collect(args: argparse.Namespace) -> dict:
    context = None
    if args.system_certs:
        import truststore

        context = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    # Reusing a caller-supplied session avoids repeated anonymous allocations.
    builders = {}
    counts = {}
    async with WomClient(session=os.environ.get("WOM_SESSION", ""), ssl_context=context) as client:

        async def observe(controller: str, payload=None) -> None:
            response = await client.request(controller, payload)
            pair = builders.setdefault(
                controller,
                {
                    "request": SchemaBuilder(schema_uri=None),
                    "response": SchemaBuilder(schema_uri=None),
                },
            )
            pair["request"].add_object(payload)
            pair["response"].add_object(response)
            counts[controller] = counts.get(controller, 0) + 1
            print(f"Observed types: {controller}")

        for user_id in args.user_id:
            await observe("GetUserInfoWS", {"userId": user_id})
        await observe("GetUserDetailDataWS", {"userId": args.user_id[-1], "popupRandId": None})
        await observe("GetRanksTableWS")
        await observe("SearchUserWS", {"query": args.query, "isFinal": False})
        await observe("SearchUserWS", {"query": str(args.user_id[-1]), "isFinal": True})
        auth = client.authorization
        assert auth is not None
        for data_type in (1, 2, 3):
            await observe(
                "FetchUserStatTableWS",
                {
                    "url": "/ranking",
                    "dataType": data_type,
                    "limit": 3 if data_type == 3 else 0,
                    "offset": 0,
                    "params": {
                        "userId": auth.user_id,
                        "season": 0,
                        "country": "",
                        "sortBy": "timePoints",
                        "brLevel": 1,
                    },
                },
            )
    return {
        "version": PROTOCOL_VERSION,
        "source_sha256": SOURCE_SHA256,
        "collected_at": datetime.now(UTC).isoformat(),
        "scope": "Public reads; JSON type schemas only, no original values or credentials",
        "apis": {
            name: {
                "samples": counts[name],
                **{
                    direction: omit_required(builder.to_schema())
                    for direction, builder in pair.items()
                },
            }
            for name, pair in sorted(builders.items())
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--system-certs", action="store_true")
    parser.add_argument("--user-id", action="append", type=int)
    parser.add_argument("--query", default="Iakuas")
    parser.add_argument("--output", type=Path, default=Path("docs/research/type-observations.json"))
    args = parser.parse_args()
    args.user_id = args.user_id or [1, 20784165]
    result = asyncio.run(collect(args))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"Stored type-only schemas for {len(result['apis'])} controllers")


if __name__ == "__main__":
    main()
