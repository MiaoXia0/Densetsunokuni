from typing import List, Callable
from hoshino import Service
from hoshino.typing import *
import os

try:
    import ujson as json
except ImportError:
    import json

sv = Service(name='Densetsunokuni')
data_dir = os.path.dirname(__file__) + '/data'
user_dir = data_dir + '/users'
equip_dir = data_dir + '/equipments'
if not os.path.exists(data_dir):
    os.mkdir(data_dir)
if not os.path.exists(user_dir):
    os.mkdir(user_dir)
try:
    equipments = json.load(open(equip_dir + '/equipments.json', 'r'))
except IOError:
    equipments = {{'id': 0, 'name': '无', 'atk': 0, 'def': 0, 'hp': 0, 'mp': 0, 'mov': 0},
                  {'id': 1, 'name': '普通的衣物', 'atk': 0, 'def': 5, 'hp': 10, 'mp': 0, 'mov': 0},
                  {'id': 2, 'name': '普通的裤子', 'atk': 0, 'def': 3, 'hp': 5, 'mp': 0, 'mov': 0},
                  {'id': 3, 'name': '普通的鞋子', 'atk': 0, 'def': 2, 'hp': 3, 'mp': 0, 'mov': 10}}
    json.dump(equipments, open(equip_dir + '/equipments.json', 'w'))
cmds: Dict[str, Callable] = {}


@sv.on_prefix('//')  # 指令执行
async def exec_cmd(bot: HoshinoBot, ev: CQEvent):
    # if ev['message_type'] != 'group':
    #     await bot.send(ev, '请在QQ群中使用本插件')
    #     return
    plain_cmd = ev.message.extract_plain_text()
    cmd, *args = plain_cmd.split(' ')  # 分割指令与参数
    if cmd in cmds:
        func = cmds[cmd]
        await func(bot, ev, args)
    elif cmd != '':
        sv.logger.info('指令列表' + str(cmds))
        await bot.send(ev, '未知指令\n输入//说明或//help查看说明')


def reg_cmd(names) -> Callable:
    if type(names) == str:
        names = [names, ]
    elif not type(names) == list:
        err_str = '指令名必须是字符串(str)或列表(list), 但却是' + str(type(names))
        raise ValueError(err_str)

    def reg(func) -> Callable:
        for name in names:
            if name in cmds:
                sv.logger.warning('命名冲突')
            else:
                cmds[name] = func
                sv.logger.info(f'[Densetsunokuni]指令{name}已注册')
        return func

    return reg
