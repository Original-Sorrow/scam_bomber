from misc import *
from aiogram import types
import handlers.keyboard as kb
from handlers.answers import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram.utils.markdown import quote_html
from .functions import *
from config import *
import re
from random import randint


def d_to_sec(days):
	return days * 24 * 60 * 60


@dp.message_handler(text=['Плюшки'])
async def profile(message: types.Message):
	user_channel_status = await bot.get_chat_member(chat_id=channel, user_id=message.chat.id)
	user_channel_status = re.findall(r"\w*", str(user_channel_status))
	time_sub = int(time.time()) + d_to_sec(1)
	data = await get_rang(message)
	if data[10]==0:
	           try:
	           	if user_channel_status[70] != 'left':
	           		cursor.execute(f'UPDATE users SET podp_time=? WHERE id=?', (time_sub, message.chat.id,))
	           		cursor.execute(f'UPDATE users SET plushka=? WHERE id=?', (1, message.chat.id,))
	           		conn.commit()
	           		await bot.send_message(message.chat.id, "Вам выдана подписка на день!")
	           		await bot.send_message(logchat, f"#new_podp\n"
	           		f"<b>Пользователь подписался на канал!</b>\n\n"
	           		f"<b>ID:</b> <code>{message.chat.id}</code>")
	           	else:
	           		await bot.send_message(message.chat.id, 'Подпишитесь на канал для получение подписки на день!',reply_markup=kb.fum)
	           except:
	           		if user_channel_status[60] != 'left':
	           			await bot.send_message(message.chat.id, "Вам выдана подписка на день!")
	           			cursor.execute(f'UPDATE users SET podp_time=? WHERE id=?', (time_sub, message.chat.id,))
	           			cursor.execute(f'UPDATE users SET plushka=? WHERE id=?', (1, message.chat.id,))
	           			conn.commit()
	           			await bot.send_message(logchat, f"#new_podp\n"
	           			f"<b>Пользователь подписался на канал!</b>\n\n"
	           			f"<b>ID:</b> <code>{message.chat.id}</code>")
	           		else:
	           			await bot.send_message(message.from_user.id, 'Подпишитесь на канал для получение подписки на день!',reply_markup=kb.fum)
	elif data[11]==0:
		await bot.send_message(message.from_user.id,f'Вы уже использовали подписку на канал для получения подписки на день, вы можете использовать промокод для получения случайного баланса\n\n <b>Промокод:</b> <code>PROMO1</code>')
	elif data[12]==0:
		await bot.send_message(message.from_user.id,f'Вы уже использовали подписку на канал для получения подписки на день, вы можете использовать промокод для получения случайного баланса\n\n <b>Промокод:</b> <code>PROMO2</code>')
	elif data[13]==0:
		await bot.send_message(message.from_user.id,f'Вы уже использовали подписку на канал для получения подписки на день, вы можете использовать промокод для получения случайного баланса\n\n <b>Промокод:</b> <code>PROMO3</code>')
	else:
		await bot.send_message(message.from_user.id,"Вы уже использовали все бонусы!")
		
@dp.message_handler(text=['PROMO1'])
async def profile(message: types.Message):
	data = await get_rang(message)
	if data[11]==0:
		pr=randint(1,10)
		bal = cursor.execute("SELECT balance FROM users WHERE id=?", (message.chat.id,)).fetchall()
		dbal = f"{int(bal[0][0])}"
		promo = int(dbal)+ int(pr)
		cursor.execute(f'UPDATE users SET balance=? WHERE id=?', (promo, message.chat.id,))
		cursor.execute(f'UPDATE users SET promo1=? WHERE id=?', (1, message.chat.id,))
		conn.commit()
		await bot.send_message(message.chat.id,f"Вы успешно использовали этот промокод!\n\nНа ваш баланс зарисленно {pr}₽")
		await bot.send_message(logchat, f"#promo\n"
		f"<b>Пользователь использовал промокод!</b>\n\n"
		f"<b>ID:</b> <code>{message.chat.id}</code>\n"
		f"<b>Получил:</b> <code>{pr}</code>₽")
	else:
		await bot.send_message(message.chat.id,"Вы уже использовали этот промокод!")		

@dp.message_handler(text=['PROMO2'])
async def profile(message: types.Message):
	data = await get_rang(message)
	if data[12]==0:
		pr=randint(1,10)
		bal = cursor.execute("SELECT balance FROM users WHERE id=?", (message.chat.id,)).fetchall()
		dbal = f"{int(bal[0][0])}"
		promo = int(dbal)+ int(pr)
		cursor.execute(f'UPDATE users SET balance=? WHERE id=?', (promo, message.chat.id,))
		cursor.execute(f'UPDATE users SET promo2=? WHERE id=?', (1, message.chat.id,))
		conn.commit()
		await bot.send_message(message.chat.id,f"Вы успешно использовали этот промокод!\n\nНа ваш баланс зарисленно {pr}₽")
		await bot.send_message(logchat, f"#promo\n"
		f"<b>Пользователь использовал промокод!</b>\n\n"
		f"<b>ID:</b> <code>{message.chat.id}</code>\n"
		f"<b>Получил:</b> <code>{pr}</code>₽")
	else:
		await bot.send_message(message.chat.id,"Вы уже использовали этот промокод!")		

@dp.message_handler(text=['PROMO3'])
async def profile(message: types.Message):
	data = await get_rang(message)
	if data[13]==0:
		pr=randint(1,10)
		bal = cursor.execute("SELECT balance FROM users WHERE id=?", (message.chat.id,)).fetchall()
		dbal = f"{int(bal[0][0])}"
		promo = int(dbal)+ int(pr)
		cursor.execute(f'UPDATE users SET balance=? WHERE id=?', (promo, message.chat.id,))
		cursor.execute(f'UPDATE users SET promo3=? WHERE id=?', (1, message.chat.id,))
		conn.commit()
		await bot.send_message(message.chat.id,f"Вы успешно использовали этот промокод!\n\nНа ваш баланс зарисленно {pr}₽")
		await bot.send_message(logchat, f"#promo\n"
		f"<b>Пользователь использовал промокод!</b>\n\n"
		f"<b>ID:</b> <code>{message.chat.id}</code>\n"
		f"<b>Получил:</b> <code>{pr}</code>₽")
	else:
		await bot.send_message(message.chat.id,"Вы уже использовали этот промокод!")																																										