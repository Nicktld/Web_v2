import orm
from models import User, Blog, Comment 
import asyncio

async def test():
    await orm.create_pool(user='Leon', password='tangledong1994', db='webv2', loop=loop)

    ul = ['Adata', 'B&K140', 'Big Tits Brother', 'Ca & Zi', 'Deepmind', 'Double lucky', 'Fa & Pe', 'LWL', 'Peace and Love', 'PriXi', 'Revenant', 'ShakeShack', 'Thursday']
    for u in ul:
        await User(name=u, email=u+'@gmail.com', passwd='000'+u[:2]+'111', image='about:black').save()

    await orm.close_pool()

async def test2():
    await orm.create_pool(user='Leon', password='tangledong1994', db='webv2', loop=loop)

    a = await User.find('00154614844968893672ba7b12c4c109d26f85734e47c15000')
    print(a.email, a.passwd, a.name)

    await orm.close_pool()
loop = asyncio.get_event_loop()
loop.run_until_complete(test2())
