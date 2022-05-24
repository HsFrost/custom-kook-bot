from khl import Bot, Message
import json
import logging
import time
import random
import requests

# 控制台日志输出
logging.basicConfig(level='INFO')

# 导入凭证json
with open('config/khl-bot-config.json', 'r', encoding='utf-8') as a, open('config/apexlegends-api.json', 'r', encoding='utf-8') as b:
    khl_bot_config = json.load(a)
    apexlegends_api = json.load(b)

# bot凭证
bot = Bot(token=khl_bot_config['token'])
# APEX api
auth=apexlegends_api['auth_key']

# 指令
@bot.command(name='hello')
async def roll(msg: Message,str:str=''):
    if str == 'time':
        await msg.reply(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    elif str == '':
        await msg.reply('world for you!')
    elif str == 'help':
        await msg.reply('什么咱们这机器人哪有那种高级功能')
    else:
        await msg.reply('Error,some thing has wrong')

@bot.command(name='apex')
async def roll(msg: Message,str:str='',player:str='',platform:str='PC'):
    solve = (requests.get(f"https://api.mozambiquehe.re/bridge?auth={auth}&player={player}&platform={platform}")).json()
    if (str=='查询') or (str==''):
        if "Error" not in solve.keys():
            player_name = solve["global"]["name"]
            player_level = solve["global"]["level"]
            player_rank = f'RANK_SCORE={solve["global"]["rank"]["rankScore"]},RANK_NAME={solve["global"]["rank"]["rankName"]}:{solve["global"]["rank"]["rankDiv"]}'
            await msg.reply(f'NAME={player_name},LEVEL={player_level},RANK={player_rank}')
        elif "Error" in solve.keys():
            await msg.reply(f'ERROR:{solve["Error"]}')
        else:
            await msg.reply("Error,some thing has wrong")
    elif str=='地图':
        await msg.reply("暂时未实装")
    else:
        await msg.reply("Exception")
#GET https://api.mozambiquehe.re/bridge?auth=YOUR_API_KEY&player=PLAYER_NAME&platform=PLATFORM

@bot.command(name='shaizi')
async def roll(msg: Message, t_min: int, t_max: int, n: int = 1):
    result = [random.randint(t_min, t_max) for i in range(n)]
    await msg.reply(f'you got: {result}')



bot.run()