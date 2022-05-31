from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from misc import *
from aiogram.types import Message
from aiogram import types
import handlers.keyboard as kb
from .functions import *
import time
import datetime
 
def d_to_sec(days):
	return days * 24 * 60 * 60






########день##########
@dp.callback_query_handler(lambda c: c.data == "buyday")
async def popol(callback_query: types.CallbackQuery):
	user = callback_query.from_user
	cursor.execute("SELECT * FROM users WHERE id=?", (user.id,))
	data = cursor.fetchone()
	result = cursor.execute("SELECT podp_time FROM users WHERE id = ?", (user.id,)).fetchall()
	for row in result:
		podp_time = int(row[0])
	if podp_time > int(time.time()):
		await bot.answer_callback_query(callback_query.id, text="У вас уже есть подписка!", show_alert=True)
	if data[2] < 30:
		await bot.answer_callback_query(callback_query.id, text="На вашем балансе недостаточно средств!", show_alert=True)
	if data[1] == 1 or data[1] == 2:
		await bot.answer_callback_query(callback_query.id, text="Ты одмен бота,тебе не надо", show_alert=True)
	else:
		coast = 30
		user = callback_query.from_user
		bal = cursor.execute("SELECT balance FROM users WHERE id=?", (user.id,)).fetchall()
		dbal = f"{int(bal[0][0])}"
		snyato = int(dbal)- int(coast)
		cursor.execute(f'UPDATE users SET balance=? WHERE id=?', (snyato, user.id,))
		time_sub = int(time.time()) + d_to_sec(1)
		cursor.execute(f'UPDATE users SET podp_time=? WHERE id=?', (time_sub, user.id,))
		conn.commit()
		await bot.answer_callback_query(callback_query.id, text="Подписка успешно преобретена!", show_alert=True)
############неделя##########
@dp.callback_query_handler(lambda c: c.data == "buyweek")
async def popol(callback_query: types.CallbackQuery):
	user = callback_query.from_user
	cursor.execute("SELECT * FROM users WHERE id=?", (user.id,))
	data = cursor.fetchone()
	result = cursor.execute("SELECT podp_time FROM users WHERE id = ?", (user.id,)).fetchall()
	for row in result:
		podp_time = int(row[0])
	if podp_time > int(time.time()):
		await bot.answer_callback_query(callback_query.id, text="У вас уже есть подписка!", show_alert=True)
	if data[2] < 200:
		await bot.answer_callback_query(callback_query.id, text="На вашем балансе недостаточно средств!", show_alert=True)
	if data[1] == 1 or data[1] == 2:
		await bot.answer_callback_query(callback_query.id, text="Ты одмен бота,тебе не надо", show_alert=True)
	else:
		coast = 200
		user = callback_query.from_user
		bal = cursor.execute("SELECT balance FROM users WHERE id=?", (user.id,)).fetchall()
		dbal = f"{int(bal[0][0])}"
		snyato = int(dbal)- int(coast)
		cursor.execute(f'UPDATE users SET balance=? WHERE id=?', (snyato, user.id,))
		time_sub = int(time.time()) + d_to_sec(7)
		cursor.execute(f'UPDATE users SET podp_time=? WHERE id=?', (time_sub, user.id,))
		conn.commit()
		await bot.answer_callback_query(callback_query.id, text="Подписка успешно преобретена!", show_alert=True)
##########месяц##########
@dp.callback_query_handler(lambda c: c.data == "buymou")
async def popol(callback_query: types.CallbackQuery):
	user = callback_query.from_user
	cursor.execute("SELECT * FROM users WHERE id=?", (user.id,))
	data = cursor.fetchone()
	result = cursor.execute("SELECT podp_time FROM users WHERE id = ?", (user.id,)).fetchall()
	for row in result:
		podp_time = int(row[0])
	if podp_time > int(time.time()):
		await bot.answer_callback_query(callback_query.id, text="У вас уже есть подписка!", show_alert=True)
	if data[2] < 500:
		await bot.answer_callback_query(callback_query.id, text="На вашем балансе недостаточно средств!", show_alert=True)
	if data[1] == 1 or data[1] == 2:
		await bot.answer_callback_query(callback_query.id, text="Ты одмен бота,тебе не надо", show_alert=True)
	else:
		coast = 500
		user = callback_query.from_user
		bal = cursor.execute("SELECT balance FROM users WHERE id=?", (user.id,)).fetchall()
		dbal = f"{int(bal[0][0])}"
		snyato = int(dbal)- int(coast)
		cursor.execute(f'UPDATE users SET balance=? WHERE id=?', (snyato, user.id,))
		time_sub = int(time.time()) + d_to_sec(30)
		cursor.execute(f'UPDATE users SET podp_time=? WHERE id=?', (time_sub, user.id,))
		conn.commit()
		await bot.answer_callback_query(callback_query.id, text="Подписка успешно преобретена!", show_alert=True)
##########2месяца###########
@dp.callback_query_handler(lambda c: c.data == "buymou2")
async def popol(callback_query: types.CallbackQuery):
	user = callback_query.from_user
	cursor.execute("SELECT * FROM users WHERE id=?", (user.id,))
	data = cursor.fetchone()
	result = cursor.execute("SELECT podp_time FROM users WHERE id = ?", (user.id,)).fetchall()
	for row in result:
		podp_time = int(row[0])
	if podp_time > int(time.time()):
		await bot.answer_callback_query(callback_query.id, text="У вас уже есть подписка!", show_alert=True)
	if data[2] < 1000:
		await bot.answer_callback_query(callback_query.id, text="На вашем балансе недостаточно средств!", show_alert=True)
	if data[1] == 1 or data[1] == 2:
		await bot.answer_callback_query(callback_query.id, text="Ты одмен бота,тебе не надо", show_alert=True)
	else:
		coast = 1000
		user = callback_query.from_user
		bal = cursor.execute("SELECT balance FROM users WHERE id=?", (user.id,)).fetchall()
		dbal = f"{int(bal[0][0])}"
		snyato = int(dbal)- int(coast)
		cursor.execute(f'UPDATE users SET balance=? WHERE id=?', (snyato, user.id,))
		time_sub = int(time.time()) + d_to_sec(60)
		cursor.execute(f'UPDATE users SET podp_time=? WHERE id=?', (time_sub, user.id,))
		conn.commit()
		await bot.answer_callback_query(callback_query.id, text="Подписка успешно преобретена!", show_alert=True)
###########полгода##########		
@dp.callback_query_handler(lambda c: c.data == "buymou6")
async def popol(callback_query: types.CallbackQuery):
	user = callback_query.from_user
	cursor.execute("SELECT * FROM users WHERE id=?", (user.id,))
	data = cursor.fetchone()
	result = cursor.execute("SELECT podp_time FROM users WHERE id = ?", (user.id,)).fetchall()
	for row in result:
		podp_time = int(row[0])
	if podp_time > int(time.time()):
		await bot.answer_callback_query(callback_query.id, text="У вас уже есть подписка!", show_alert=True)
	if data[2] < 2500:
		await bot.answer_callback_query(callback_query.id, text="На вашем балансе недостаточно средств!", show_alert=True)
	if data[1] == 1 or data[1] == 2:
		await bot.answer_callback_query(callback_query.id, text="Ты одмен бота,тебе не надо", show_alert=True)
	else:
		coast = 2500
		user = callback_query.from_user
		bal = cursor.execute("SELECT balance FROM users WHERE id=?", (user.id,)).fetchall()
		dbal = f"{int(bal[0][0])}"
		snyato = int(dbal)- int(coast)
		cursor.execute(f'UPDATE users SET balance=? WHERE id=?', (snyato, user.id,))
		time_sub = int(time.time()) + d_to_sec(180)
		cursor.execute(f'UPDATE users SET podp_time=? WHERE id=?', (time_sub, user.id,))
		conn.commit()
		await bot.answer_callback_query(callback_query.id, text="Подписка успешно преобретена!", show_alert=True)
###########навсегда###########		
@dp.callback_query_handler(lambda c: c.data == "buyall")
async def popol(callback_query: types.CallbackQuery):
	user = callback_query.from_user
	cursor.execute("SELECT * FROM users WHERE id=?", (user.id,))
	data = cursor.fetchone()
	result = cursor.execute("SELECT podp_time FROM users WHERE id = ?", (user.id,)).fetchall()
	for row in result:
		podp_time = int(row[0])
	if podp_time > int(time.time()):
		await bot.answer_callback_query(callback_query.id, text="У вас уже есть подписка!", show_alert=True)
	if data[2] < 5000:
		await bot.answer_callback_query(callback_query.id, text="На вашем балансе недостаточно средств!", show_alert=True)
	if data[1] == 1 or data[1] == 2:
		await bot.answer_callback_query(callback_query.id, text="Ты одмен бота,тебе не надо", show_alert=True)
	else:
		coast = 5000
		user = callback_query.from_user
		bal = cursor.execute("SELECT balance FROM users WHERE id=?", (user.id,)).fetchall()
		dbal = f"{int(bal[0][0])}"
		snyato = int(dbal)- int(coast)
		cursor.execute(f'UPDATE users SET balance=? WHERE id=?', (snyato, user.id,))
		cursor.execute(f'UPDATE users SET podpiska=? WHERE id=?', (1, user.id,))
		conn.commit()
		await bot.answer_callback_query(callback_query.id, text="Подписка успешно преобретена!", show_alert=True)																																																																																																																																																						