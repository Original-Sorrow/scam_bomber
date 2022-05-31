from misc import *
from aiogram.types import Message
from aiogram.utils.markdown import quote_html
from aiogram import types
from .functions import *
import handlers.keyboard as kb
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import time
import datetime



@dp.message_handler(text=['Профиль'])
async def profile(message: types.Message):
    user = message.from_user
    chat = message.chat
    data = await get_rang(message)
    if data[1] == 2:
            status = "\n\n«<b>Кодер бота</b>»"
    elif data[1] == 1:
            status = "\n\n«<b>Админ бота</b>»"
    elif data[1] == 0:
            status = ""
    balance = await get_balance(message)
    user_sub = time_sub(message)
    sstat = get_sub_status(message)
    if data[4] == 1:
    	podp = "навсегда😎"
    else:
    	if sstat == False :
    		podp= "нема"
    	else:
    		podp = f"осталось <code>{user_sub}</code>"
    if user.username is None:
            username = "Отсутствует"
    else:
            username = f"@{user.username}"
            
    await bot.send_message(message.chat.id,
    f"<b>Основная информация:</b>\n\n"
      f"<b>💬Имя:</b> {quote_html(user.full_name)}\n"
      f"<b>💬Юзернейм:</b> {username}\n"
      f"<b>💬ID:</b> <code>{user.id}</code>\n\n"
      f"<b>💸Баланс:</b> <code>{balance}</code>₽\n"
      f"<b>💲Подписка:</b> {podp}"
      f"{status}", reply_markup=kb.prof)