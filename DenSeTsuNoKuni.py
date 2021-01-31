from typing import List, Callable
from hoshino import Service
from hoshino.typing import *
import os

sv = Service(name='densetsunokuni')

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
        return func

    return reg
