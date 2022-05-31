from misc import bot, dp
from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram import Bot, Dispatcher, executor, types
import handlers.keyboard as kb
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from .functions import *

@dp.message_handler(text=['Инфо'])
async def fag(message: types.Message):
    user = message.from_user
    data = await get_rang(message)
    if data[1] == 2 or data[1] == 1:
        users = await get_len_users(message)
        podp = await get_len_podp(message)
        await bot.send_message(message.chat.id, f"<b>Информация о базе данных бота:</b>\n\n"
        f"Зарегистрированных пользователей: <code>{users}</code>\n",reply_markup=kb.fagadm)
    else:
     	await bot.send_message(message.chat.id, f'Информация о боте находиться ниже', reply_markup=kb.fag)     	     	     	     			     	