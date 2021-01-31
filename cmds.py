from hoshino.typing import *
from .DenSeTsuNoKuni import reg_cmd
from .texts import *


@reg_cmd('测试输出')
async def cmd_test(bot: HoshinoBot, ev: CQEvent, args):
    for i in args:
        await bot.send(ev, str(i))


@reg_cmd(['说明', 'help'])
async def cmd_desc(bot: HoshinoBot, ev: CQEvent, args):
    await bot.send(ev, desc)


@reg_cmd(['菜单', 'menu'])
async def cmd_menu(bot: HoshinoBot, ev: CQEvent, args):
    await bot.send(ev, menu)
