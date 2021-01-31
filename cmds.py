from hoshino.typing import *
from .DenSeTsuNoKuni import reg_cmd
from .texts import *
import os
try:
    import ujson as json
except ImportError:
    import json

data_dir = os.path.dirname(__file__) + '/data'
user_dir = data_dir + '/users'


def isUserExist(QQ: str):
    try:
        json.load(open(user_dir + f'/{QQ}.json', 'r'))
    except IOError:
        return False
    else:
        return True


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


@reg_cmd('创建角色')
async def cmd_create(bot: HoshinoBot, ev: CQEvent, args):
    try:
        name = args[0]
    except IndexError:
        name = ''
    user_id = ev['user_id']
    if name == '':
        await bot.send(ev, '请输入//创建角色 角色名')
        return
    if isUserExist(user_id):
        await bot.send(ev, '您已创建角色！')
        return
    new_user = {'name': name, 'level': 0, 'exp': 0}
    json.dump(open(user_dir + f'{user_id}.json', 'w'))
    await bot.send(ev, f'角色{name}已创建，欢迎来到传说的国度！')
