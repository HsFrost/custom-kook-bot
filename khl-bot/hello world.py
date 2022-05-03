from khl import Bot, Message
import random
import json
import logging
#控制台日志输出
logging.basicConfig(level='INFO')


#导入凭证json
with open('config\config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

#bot凭证
bot = Bot(token=config['token'])



@bot.command(prefix=['.'],name='hello')
async def roll(msg: Message):
    # quote reply
    await msg.reply('world for you!')


bot.run()