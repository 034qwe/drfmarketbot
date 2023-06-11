from aiogram.utils import executor
from createbot import dp
from handlers import myorder


async def on_startup(_):
    print('bot start')


myorder.register_handlers_myorder(dp)

    
executor.start_polling(dp, skip_updates=True,on_startup=on_startup)