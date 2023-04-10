import logging
import time
import os
import aiogram
from aiogram import Bot,Dispatcher,types,executor

TOKEN=os.getenv('TOKEN')
bot=Bot(token=TOKEN)
dp=Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_welcome(message:types.Message):
    user_id = message.from_user.id
    user_name=message.from_user.full_name
    logging.info(f"{user_id=} {user_name=} {time.asctime()}")
    await message.reply(f'{user_name},nice to see you. What would you like to translit?')
@dp.message_handler()
async def send_translit(message:types.Message):
    user_name = message.from_user.full_name 
    user_id = message.from_user.id
    original_text = message.text
    x = {'А':'A', 'Б':'B', 'В':'V', 'Г':'G', 'Д':'D', 'Е':'E', 'Ё':'E', 'Ж':'ZH', 'З':'Z', 'И':'I', 'Й':'I', 
'К':'K', 'Л':'L', 'М':'M', 'Н':'N', 'О':'O', 'П':'P', 'Р':'R', 'С':'S', 'Т':'T', 'У':'U', 'Ф':'F', 
   'Х':'KH', 'Ц':'TS', 'Ч':'Ch', 'Ш':'SH', 'Щ':'SHCH', 'Ы':'Y', 'Ъ':'IE', 'Э':'E', 'Ю':'IU', 'Я':'IA','Ь':''}
    result=''
    for i in original_text:
        mytable=str.maketrans(x)
        if i == i.upper():
            result+=i.translate(mytable)
        elif i == i.lower():
            new_i=i.upper()
            new_i=new_i.translate(mytable)
            new_i=new_i.lower()
            result+=new_i
    logging.info(f"{user_name=} {user_id=} sent_message: {original_text} {result}")
    await bot.send_message(user_id, result)
if __name__ == '__main__':
    executor.start_polling(dp)