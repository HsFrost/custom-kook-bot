import json
import logging
import time
import random
import requests

from khl import Bot, Message, EventTypes, Event
from khl.card import CardMessage, Card, Module, Element, Types, Struct


# 控制台日志输出
logging.basicConfig(level='INFO')


# 导入凭证json
with open('config/khl-bot-config.json', 'r', encoding='utf-8') as a, open('config/apexlegends-api.json', 'r', encoding='utf-8') as b:
    khl_bot_config = json.load(a)
    apexlegends_api = json.load(b)


# bot凭证
bot = Bot(token=khl_bot_config['token'])
# APEX api凭证
auth=apexlegends_api['auth_key']



# hello指令
@bot.command(name='hello')
async def hello(msg: Message,str:str=''):
    '''
    :param msg: (忽略)
    :param str: 指令['','time','help']
    :return:
    '''
    if str == '':
        await msg.reply('world for you!')
    elif str == 'time':
        await msg.reply(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    elif str == 'help':
        await msg.reply('什么咱们这机器人哪有那种高级功能')
    else:
        await msg.reply('Error,some thing has wrong')

# apex战绩查询
@bot.command(name='apex')
async def apex(msg: Message,str:str='',player:str='',platform:str='PC'):
    '''
    :param msg: (默认值)
    :param str: 指令
    :param player: 玩家ID
    :param platform: 玩家平台 ['PC'(Origin or Steam),'PS4'(Playstation 4/5) or 'X1'(Xbox)]
    :return:
    '''

    if str=='查询':
        #solve为向api发送请求的返回解
        solve = (requests.get(f"https://api.mozambiquehe.re/bridge?auth={auth}&player={player}&platform={platform}")).json()
        if "Error" not in solve.keys():

            #几组玩家参数
            player_name = solve["global"]["name"]
            player_level = solve["global"]["level"]
            player_rank = f'{solve["global"]["rank"]["rankName"]}{solve["global"]["rank"]["rankDiv"]}_{solve["global"]["rank"]["rankScore"]}'

            #回复
            cm = CardMessage()
            c1 = Card(color='#000000')
            c1.append(
            Module.Header('查询结果：'),
            Module.Divider(),
            Module.Header(f'{player_name},{player_level}')
            )
            cm.append(c1)


            c2 = Card(color='#000000')
            c2.append(
            Module.Container(
                Element.Image(src=solve["legends"]["selected"]["ImgAssets"]["icon"]),
                Element.Image(src=solve["global"]["rank"]["rankImg"]),
            ),
            Module.Header(f'{player_rank}')
            )
            cm.append(c2)

            await msg.reply(cm)

        elif "Error" in solve.keys():
            await msg.reply(f'ERROR:{solve["Error"]}')
        else:
            await msg.reply("Error,some thing has wrong")
    elif str=='地图':
        await msg.reply("暂时未实装")
    elif str=='帮助':
        await msg.reply("暂时未实装")
    else:
        await msg.reply("Command not Found")
#GET https://api.mozambiquehe.re/bridge?auth=YOUR_API_KEY&player=PLAYER_NAME&platform=PLATFORM




#掷色子
@bot.command(name='roll')
async def roll(msg: Message, t_min: int, t_max: int, n: int = 1):
    '''
    :param msg: （忽略）
    :param t_min: 色子的最小点数
    :param t_max: 色子的最大点数
    :param n:     色子掷几次
    :return:
    '''
    result = [random.randint(t_min, t_max) for i in range(n)]
    await msg.reply(f'you got: {result}')



bot.run()