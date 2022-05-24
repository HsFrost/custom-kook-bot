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
async def roll(msg: Message,player:str='',platform:str='PC'):
    if player != '':
        solve = (requests.get(f"https://api.mozambiquehe.re/bridge?auth={auth}&player={player}&platform={platform}")).json()
        await msg.reply(f'NAME={solve["global"]["name"]},LEVEL={solve["global"]["level"]}')
    elif player == '':
        await msg.reply("Error,can't solve,maby you did not input PlayerNAME.")

#GET https://api.mozambiquehe.re/bridge?auth=YOUR_API_KEY&player=PLAYER_NAME&platform=PLATFORM

@bot.command(name='shaizi')
async def roll(msg: Message, t_min: int, t_max: int, n: int = 1):
    result = [random.randint(t_min, t_max) for i in range(n)]
    await msg.reply(f'you got: {result}')



bot.run()