from re import search
from aiogram import Dispatcher,types
from createbot import dp,bot



async def Hello_send(message: types.Message):
    await  bot.send_message(message.from_user.id,f'Hello {message.from_user.first_name}')




def register_handlers_myorder(dp: Dispatcher):
    dp.register_message_handler(Hello_send,commands=['start'])