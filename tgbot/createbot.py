from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage= MemoryStorage()
TOKEN = '6068566463:AAGzmuIKI5CWjgld7jh0_QhYJFkv5MJ2IxE'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot,storage=storage)