from khl import Bot, Message
import random
import json
import logging
import time
#控制台日志输出
logging.basicConfig(level='INFO')


#导入凭证json
with open('config\config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

#bot凭证
bot = Bot(token=config['token'])



@bot.command(name='hello')
async def roll(msg: Message,str:str=''):
    if str == 'time':
        await msg.reply(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    elif str == '':
        await msg.reply('world for you!')
    elif str == 'help':
        await msg.reply('什么咱们这机器人哪有那种高级功能')
    else:
        await msg.reply('Error')
@bot.command(name='shaizi')
async def roll(msg: Message, t_min: int, t_max: int, n: int = 1):
    result = [random.randint(t_min, t_max) for i in range(n)]
    await msg.reply(f'you got: {result}')



bot.run()