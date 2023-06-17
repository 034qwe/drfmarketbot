from aiogram.utils import executor
from createbot import dp
from handlers import myorder
from aiogram.contrib.fsm_storage.memory import MemoryStorage


async def on_startup(_):
    print('bot start')


storage = MemoryStorage()


myorder.register_handlers_myorder(dp)

    
executor.start_polling(dp, skip_updates=True,on_startup=on_startup)