import json
import logging
import time
import random
import requests

from khl import Bot, Message
from khl.card import CardMessage, Card, Module, Element, Types

import command_hello_help

# 控制台日志输出
logging.basicConfig(level='INFO')

# 导入凭证json
with open('config/khl_bot_config.json', 'r', encoding='utf-8') as a, open('config/apex_legends_api.json', 'r',
                                                                          encoding='utf-8') as b:
    khl_bot_config = json.load(a)
    apex_legends_api = json.load(b)

# bot凭证
bot = Bot(token=khl_bot_config['token'])
# APEX api凭证
auth = apex_legends_api['auth_key']

# 命令符号
PREFIX = ['.']


# hello指令
@bot.command(name='hello', prefixes=PREFIX)
async def hello(msg: Message, term: str = ''):

    # :param msg: (忽略)
    # :param term: 指令['','time','help']
    # :return:

    if term == '':
        await msg.reply('world for you!')
    elif term == 'time':
        await msg.reply(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    elif term == 'help':
        await msg.reply(
            CardMessage(Card(
                Module.Header('帮助文档'),
                Module.Divider(),
                Module.Section(Element.Text(command_hello.help(),type=Types.Text.KMD)),
                Module.Divider(),
                color='#0DFF94'),
            )
        )
    else:
        await msg.reply('Error,some thing has wrong')


# apex战绩查询
@bot.command(name='apex', prefixes=PREFIX)
async def apex(msg: Message, term: str = '', player: str = '', platform: str = 'PC'):

    # :param msg: (默认值)
    # :param term: 指令
    # :param player: 玩家ID
    # :param platform: 玩家平台 ['PC'(Origin or Steam),'PS4'(Playstation 4/5) or 'X1'(Xbox)]
    # :return:

    if term == '查询':
        # solve为向api发送请求的返回解
        # GET https://api.mozambiquehe.re/bridge?auth=YOUR_API_KEY&player=PLAYER_NAME&platform=PLATFORM
        solve = (
            requests.get(f"https://api.mozambiquehe.re/bridge?auth={auth}&player={player}&platform={platform}")).json()
        if "Error" not in solve.keys():
            # 几组玩家参数
            player_name = f'玩家：{solve["global"]["name"]}'
            player_level = f'等级：{solve["global"]["level"]}'
            player_rank = f'段位：{solve["global"]["rank"]["rankName"]}{solve["global"]["rank"]["rankDiv"]}:'\
                          f'{solve["global"]["rank"]["rankScore"]} '
            player_rank_icon = f'{solve["global"]["rank"]["rankImg"]}'
            player_player = f'{solve["legends"]["selected"]["LegendName"]}'
            player_player_icon = f'{solve["legends"]["selected"]["ImgAssets"]["icon"]}'
            # 回复
            await msg.reply(
                CardMessage(Card(
                    # 子项
                    Module.Header('查询结果：'),
                    # 分割线
                    Module.Divider(),
                    # 子项
                    Module.Section(f'{player_name}\n{player_level}\n{player_rank}',
                                   accessory=Element.Image(src=f'{player_rank_icon}'),
                                   mode=Types.SectionMode.RIGHT),
                    # 子项
                    Module.Divider(),
                    # 子项
                    Module.Section(f'常用角色:{player_player}'),
                    # 子项
                    Module.Container(Element.Image(src=f'{player_player_icon}')),
                    # 颜色设置
                    color='#DE1717'))
            )
        # 选择支
        elif "Error" in solve.keys():
            await msg.reply(f'ERROR:{solve["Error"]}')
        # 选择支
        else:
            await msg.reply("Error,some thing has wrong")
    # 选择支
    elif term == '地图':
        await msg.reply("暂时未实装")
    # 选择支
    elif term == '帮助':
        await msg.reply("暂时未实装")
    # 选择支
    else:
        await msg.reply("Command not Found")


# 掷色子
@bot.command(name='roll', prefixes=PREFIX)
async def roll(msg: Message, t_min: int, t_max: int, n: int = 1):

    # :param msg: （忽略）
    # :param t_min: 色子的最小点数
    # :param t_max: 色子的最大点数
    # :param n:     色子掷几次
    # :return:

    result = [random.randint(t_min, t_max) for i in range(n)]
    await msg.reply(f'you got: {result}')


bot.run()
