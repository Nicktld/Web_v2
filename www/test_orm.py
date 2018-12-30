import orm
from models import Team
import asyncio

async def test():
    await orm.create_pool(user='webapp', password='tangledong1994', db='ee627', loop=loop)

    tl = ['Adata', 'B&K140', 'Big Tits Brother', 'Ca & Zi', 'Deepmind', 'Double lucky', 'Fa & Pe', 'LWL', 'Peace and Love', 'PriXi', 'Revenant', 'ShakeShack', 'Thursday']
    for t in tl:
        await Team(name=t).save()

    await orm.close_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test())

