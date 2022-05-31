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

@dp.message_handler(text=['Начать атаку'])
async def profile(message: types.Message):
    user = message.from_user
    chat = message.chat
    data = await get_rang(message)
    user_sub = time_sub(message)
    sstat = get_sub_status(message)
    if data[4] == 1 or sstat == True:
    	await bot.send_message(message.chat.id,"Введите номер для спама:")
    else:
    	await bot.send_message(message.chat.id,f"{quote_html(user.full_name)}, у вас отсутствует подписка, необходимо приобрести её для раюоты с ботом!", reply_markup=kb.prof)    	