import requests
from re import search
from aiogram import Dispatcher,types
from createbot import dp,bot
from fake_useragent import UserAgent

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup



async def Hello_send(message: types.Message):
    

    await  bot.send_message(message.from_user.id,f'Hello {message.from_user.first_name}')

    try:
        print(auth_token)
    except:
        await message.answer(f'please login \n command: /reg')


class RegistrationStates(StatesGroup):
    waiting_username = State()
    waiting_password = State()


async def start_handler(message: types.Message):
    try:
        if auth_token:
            await message.answer('you are already registered')
    except:
        await RegistrationStates.waiting_username.set()
        await message.reply("enter your username:")


async def username_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text

    await RegistrationStates.next()
    await message.reply("enter your password:")


async def password_handler(message: types.Message, state: FSMContext):
    global auth_token
    async with state.proxy() as data:
        data['password'] = message.text

    async with state.proxy() as data:
        username = data['username']
        password = data['password']


        try:
            auth_token = await login(username=username,password=password)
            await message.answer('you registered')
        except:
            await message.answer('incorrect password or username')


    await state.finish()


async  def login(username,password):
    headers = {
                'User-Agent': UserAgent().random,
            }
    data = {
        'username': username,
        'password': password
    }

    response = requests.post('http://127.0.0.1:8000/auth/token/login/',headers=headers,data=data)
    orders = response.json()

    return str(orders['auth_token'])


async def test(message: types.Message):
    headers = {
                'User-Agent': UserAgent().random,
                'Authorization': f'Token {auth_token}'
            }

    response = requests.get('http://127.0.0.1:8000/myorder/',headers=headers)
    orders = response.json()

    [ await message.answer(i['product']['images'][0]['image']["full_size"]) for i in orders]





####
def register_handlers_myorder(dp: Dispatcher):
    dp.register_message_handler(Hello_send,commands=['start'])
    dp.register_message_handler(test,commands=['order'])
    dp.register_message_handler(login,commands=['login'])
    dp.register_message_handler(start_handler,commands=['reg'])
    dp.register_message_handler(username_handler,state=RegistrationStates.waiting_username)
    dp.register_message_handler(password_handler,state=RegistrationStates.waiting_password)


