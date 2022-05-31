from misc import *
from aiogram import types
import handlers.keyboard as kb
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram.utils.markdown import quote_html
from .functions import *
from config import *

@dp.message_handler(commands=['adm'])
async def cmd_adm(message: types.Message):
	data = await get_rang(message)
	users = await get_len_users(message)
	if data[1] == 2 or data[1] ==1:
	       if data[1] == 2:
	           status = "«<b>Кодер бота</b>»"
	           voz = '''/setadmin (id) - назначение админов бота
/deladmin (id) - удаление админов бота
/rsl (текст) - рассылка по лс'''
	       elif data[1] == 1:
	       	status = "«<b>Админ бота</b>»"
	       	voz = "нтхуя"
	       await bot.send_message(message.chat.id, f"<b>Информация:</b>\n\n"
	       f"Зарегистрированных пользователей: <code>{users}</code>\n"
	       f"Твой ранг: {status}\n\n"
	       f"<b>Ты можешь:</b>\n\n"
	       f"{voz}",reply_markup=kb.delete)




@dp.message_handler(commands=['setadmin'])
async def cmd_setadmin(message: types.Message):
	args = message.get_args()
	data = await get_rang(message)
	user = int(args)
	if data[1] == 2:
		cursor.execute(f'UPDATE users SET rang=? WHERE id=?', (1, user,))
		conn.commit()
		await bot.send_message(message.chat.id,"Готово!")
		await bot.send_message(logchat, f"#new_adm_sakura\n"
		f"<b>Новый админ бота!</b>\n\n"
		f"<b>ID:</b> <code>{user}\n</code>"
		f"Назначил: <code>{message.chat.id}</code>")
	else:
	       pass

@dp.message_handler(commands=['deladmin'])
async def cmd_deladmin(message: types.Message):
	args = message.get_args()
	data = await get_rang(message)
	user = int(args)
	if data[1] == 2:
		cursor.execute(f'UPDATE users SET rang=? WHERE id=?', (0, user,))
		conn.commit()
		await bot.send_message(message.chat.id,"Готово!")
		await bot.send_message(logchat, f"#new_adm_snyat_sakura\n"
		f"<b>Новый админ бота получил пиздов !</b>\n\n"
		f"<b>ID:</b> <code>{user}\n</code>"
		f"Дал пизды: <code>{message.chat.id}</code>")
	else:
	       pass
	       
@dp.message_handler(commands=['rsl'])
async def cmd_rsl(message: types.Message):
    user = message.from_user
    args = message.get_args()
    data = await get_rang(message)
    if data[1] == 2:
        if not args:
            await message.reply("Укажи аргументы.")
        else:
            chats = cursor.execute("SELECT id FROM users").fetchall()
            for x in chats:
                try:
                    chat = await bot.get_chat(str(x[0]))
                    await bot.send_message(chat.id, args)
                except: pass

            await message.reply("Рассылка успешна!")
            await bot.send_message(logchat, f"#new_rsl_sakura\n"
            f"НОВАЯ РАССЫЛКА В БОТЕ\n\n"
            f"Провёл: <code>{user.id}</code>\n"
            f"Текст рассылки: <code>{args}</code>")	                                       