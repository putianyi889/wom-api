"""Opt-in smoke check against the website; no tests contact it automatically."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import ssl

from wom_api import WomClient


async def main(args: argparse.Namespace) -> None:
    context = None
    if args.system_certs:
        import truststore

        context = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    async with WomClient(session=os.environ.get("WOM_SESSION", ""), ssl_context=context) as client:
        profile = await client.get_user_info(userId=args.user_id)
        assert isinstance(profile, dict) and isinstance(profile.get("user"), dict)
        assert profile["user"]["id"] == args.user_id
        print("GetUserInfoWS: verified user ID")
        ranks = await client.get_ranks_table()
        assert isinstance(ranks, dict) and isinstance(ranks.get("ranksCount"), dict)
        print("GetRanksTableWS: verified ranksCount")
        auth = client.authorization
        assert auth is not None
        ranking = await client.fetch_user_stat_table(
            {
                "url": "/ranking",
                "dataType": 3,
                "limit": 3,
                "offset": 0,
                "params": {
                    "userId": auth.user_id,
                    "season": 0,
                    "country": "",
                    "sortBy": "timePoints",
                    "brLevel": 1,
                },
            }
        )
        assert isinstance(ranking, dict) and isinstance(ranking.get("rows"), list)
        print(f"FetchUserStatTableWS: verified {len(ranking['rows'])} rows")
        print(f"Socket.IO ping: {await client.ping():.3f}s")
        assert await client.ping_http() == "OK"
        print("HTTP /ping: verified OK")
        if args.game_id:
            game = await client.get_game(args.game_id)
            assert isinstance(game[0], dict) and game[0]["id"] == args.game_id
            print(
                f"EnterGameWS/InitGameEvent: verified {len(game)} arguments, "
                f"{len(json.dumps(game))} JSON characters"
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--user-id", type=int, default=1)
    parser.add_argument("--game-id", type=int)
    parser.add_argument("--system-certs", action="store_true")
    asyncio.run(main(parser.parse_args()))
