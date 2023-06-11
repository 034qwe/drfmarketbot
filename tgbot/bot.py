from aiogram.utils import executor
from createbot import dp



async def on_startup(_):
    print('bot start')




    
executor.start_polling(dp, skip_updates=True,on_startup=on_startup)