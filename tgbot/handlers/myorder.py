import requests
from re import search
from aiogram import Dispatcher,types
from createbot import dp,bot
from fake_useragent import UserAgent




passsword = '1234'
usernamee = 'owner'

async  def login():
    headers = {
                'User-Agent': UserAgent().random,


            }
    data = {
        'username': usernamee,
        'password': passsword
    }

    response = requests.post('http://127.0.0.1:8000/auth/token/login/',headers=headers,data=data)
    orders = response.json()




    return str(orders['auth_token'])





passsword = '1234'
usernamee = 'owner'

async def Hello_send(message: types.Message):
    global auth_token
    auth_token = await login()
    ###
    print(auth_token)
    ###

    await  bot.send_message(message.from_user.id,f'Hello {message.from_user.first_name}')

    if auth_token:
        pass
    else:
        await message.answer('please login')



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