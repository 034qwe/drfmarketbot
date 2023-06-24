
import asyncio

from handlers import myorder
from handlers.myorder import *

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = '6068566463:AAGzmuIKI5CWjgld7jh0_QhYJFkv5MJ2IxE'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

async def main():
    

    myorder.register_handlers_myorder(dp)

    asyncio.create_task(fetch_orders())
    
    await dp.start_polling()
    print('bot start')


if __name__ == "__main__":
    asyncio.run(main())





# from aiogram.utils import executor
# from createbot import dp
# from handlers import myorder
# from aiogram.contrib.fsm_storage.memory import MemoryStorage


# async def on_startup(_):
#     print('bot start')





# myorder.register_handlers_myorder(dp)

    
# executor.start_polling(dp, skip_updates=True,on_startup=on_startup)
