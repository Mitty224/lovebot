# the love maker bot  for my domestic gf

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from config import TOKEN
from aiogram.utils.markdown import hbold
import logging
import sys
from aiogram.filters import CommandStart, Command
from random import choice
from hearts import HEART, COLORED_HEARTS, PARADE_MAP, FIRST_H


dp = Dispatcher()

def love_in_love(HEART, COLORED_HEARTS, PARADE_MAP):
    output = ''
    for i in PARADE_MAP:
        if i == '0':
            output += HEART
        elif i == '1':
            output += choice(COLORED_HEARTS)
        else:
            output += i
    return output

async def send_love(message: Message, bot: Bot):
    sent = await message.answer('for you')
    for i in FIRST_H:
        await bot.edit_message_text(chat_id=message.chat.id, message_id=sent.message_id, text=i)
        await asyncio.sleep(1)
    await asyncio.sleep(1)
    for i in range(30):
        await bot.edit_message_text(chat_id=message.chat.id, message_id=sent.message_id,
                                    text=love_in_love(HEART, COLORED_HEARTS, PARADE_MAP))
        await asyncio.sleep(0.2)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=sent.message_id, text='❤️️️️️️️')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=sent.message_id, text='love')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=sent.message_id, text='love you')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=sent.message_id, text='love you💗')


async def start():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    bot = Bot(token=TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    dp.message.register(start_command, Command(commands=['start', 'run']))
    dp.message.register(send_love)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

@dp.message(CommandStart())
async def start_command(message: Message, bot: Bot):
    await message.answer(f"Hi, {hbold(message.from_user.full_name)}, i`m love maker bot.\n"
                         f"Send a message to receive something.")



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(start())
