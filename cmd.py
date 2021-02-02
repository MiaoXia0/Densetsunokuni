from hoshino.typing import *
from .Densetsunokuni import *
from .texts import *
import os

try:
    import ujson as json
except ImportError:
    import json


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
    new_user = {'name': name,
                'level': 0,
                'exp': 0,
                'hp': 100,
                'mp': 20,
                'atk': 10,
                'def': 0,
                'mov': 100,
                'equipments': {'head': 0,
                               'body': 1,
                               'hand': 0,
                               'leg': 2,
                               'foot': 3
                               }
                }
    json.dump(new_user, open(user_dir + f'/{user_id}.json', 'w'))
    await bot.send(ev, f'角色{name}已创建，欢迎来到传说的国度！')


@reg_cmd('删除角色')
async def cmd_delete(bot: HoshinoBot, ev: CQEvent, args):
    user_id = ev['user_id']
    if not isUserExist(user_id):
        await bot.send(ev, '您未创建角色！')
        return
    else:
        os.remove(user_dir + f'/{user_id}.json')
        await bot.send(ev, '角色已删除！')
