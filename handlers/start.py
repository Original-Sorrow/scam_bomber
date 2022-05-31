from misc import bot, dp
from aiogram import types
import handlers.keyboard as kb
from handlers.answers import start
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram.utils.markdown import quote_html
from .functions import *
from config import *


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
         user = new_user(message.chat.id)
         photo = open('Media/start.webp','rb')
         data = await get_rang(message)
         if user == 'new user':
         	await bot.send_sticker(message.chat.id,photo,reply_markup=kb.menu)
         	await bot.send_message(message.chat.id,start,reply_markup=kb.start)
         	await bot.send_message(message.chat.id,"- powered by FUM",reply_markup=kb.fum)
         	await bot.send_message(message.chat.id,'''- coded by @Original_Sorrow with love ❤️''')
         	user = message.from_user
         	await bot.send_message(logchat, f"#new_user_sakura\n"

         	f"<b>Новый пользователь в базе данных!</b>\n\n"

         	f"• <b>Name:</b> <a href='tg://user?id={user.id}'>{user.first_name}</a>\n"
         	f"• <b>ID:</b> <code>{user.id}</code>")

         else:
         			if data[1] == 2 or data[1] == 1:
         				await bot.send_sticker(message.chat.id,photo,reply_markup=kb.menu)
         			else:
         				await bot.send_sticker(message.chat.id,photo,reply_markup=kb.menu)
         				await bot.send_message(message.chat.id,start,reply_markup=kb.start)
         				await bot.send_message(message.chat.id,"- powered by FUM",reply_markup=kb.fum)
         				await bot.send_message(message.chat.id,'''- coded by @Original_Sorrow with love ❤️''')         			         		         			      