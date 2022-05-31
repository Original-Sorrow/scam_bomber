from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from misc import *
from aiogram.types import Message
from aiogram import types
import handlers.keyboard as kb    
from aiogram.utils.helper import Helper, HelperMode, ListItem
                                      
@dp.callback_query_handler(lambda c: c.data == "delete")
async def delete(callback_query: types.CallbackQuery):
	await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
		                    
@dp.callback_query_handler(lambda c: c.data == "show")
async def show(callback_query: types.CallbackQuery):
	await bot.send_message(callback_query.message.chat.id,f'Информация о боте находиться ниже', reply_markup=kb.fag)

@dp.callback_query_handler(lambda c: c.data == "kyp")
async def kyp(callback_query: types.CallbackQuery):
	user = callback_query.from_user
	cursor.execute("SELECT * FROM users WHERE id=?", (user.id,))
	data = cursor.fetchone()
	if data[4] == 1:
		await bot.answer_callback_query(callback_query.id, text="У вас подписка навсегда, вам не нужно покупать!", show_alert=True)
	else:
		await bot.send_message(callback_query.message.chat.id,f'Выберете вариант подписки', reply_markup=kb.buy)
	
@dp.callback_query_handler(lambda c: c.data == "popol")
async def popol(callback_query: types.CallbackQuery):
	await bot.send_message(callback_query.message.chat.id,f"Выберете сумму пополнения",reply_markup=kb.pay)