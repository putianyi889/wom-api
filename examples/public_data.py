"""Read a profile and public ranking. Run with: python examples/public_data.py."""

import asyncio

from wom_api import WomClient


async def main() -> None:
    async with WomClient() as client:
        profile = await client.get_user_info(userId=1)
        print(profile)
        auth = client.authorization
        assert auth is not None
        ranking = await client.fetch_user_stat_table(
            {
                "url": "/ranking",
                "dataType": 3,
                "limit": 10,
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
        print(ranking)


if __name__ == "__main__":
    asyncio.run(main())
