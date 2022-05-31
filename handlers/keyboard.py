from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
############кнопачки обычные#######
menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(types.KeyboardButton('Начать атаку'))
menu.row('Инфо','Профиль','Плюшки')
############инлайн кнопачки########
###########правила в преветственном смс###########
rule_keyboard = types.InlineKeyboardMarkup()
rule = types.InlineKeyboardButton('Правила', url="https://telegra.ph/PRAVILA-03-20-15")
start = rule_keyboard.add(rule)
 ############подпишитесь на канал######
fum_keyboard = types.InlineKeyboardMarkup()
fum = types.InlineKeyboardButton('FUM PRODUCTION', url="https://t.me/F_U_M_channel")
fum = fum_keyboard.add(fum)
############меню фаг######
inline_keyboard = types.InlineKeyboardMarkup()
rule = types.InlineKeyboardButton('Правила', url="https://telegra.ph/PRAVILA-03-20-15")
chego = types.InlineKeyboardButton('Для чего этот бот?', url="https://telegra.ph/Dlya-chego-ehtot-bot-03-20")
podp = types.InlineKeyboardButton('Всё про подписки', url="https://telegra.ph/Skolko-stoit-i-kak-kupit-podpisku-03-20")
adm = types.InlineKeyboardButton('Владелец бота', url="https://t.me/uuiuuka")
coder = types.InlineKeyboardButton('Хочу такого же бота/кто кодер?', url="https://t.me/Original_Sorrow")
fag = inline_keyboard.add(rule).add(chego).add(podp).add(adm).add(coder)
##########профиль#########
inline_keyboard = types.InlineKeyboardMarkup()
popol = InlineKeyboardButton('Пополнить баланс', callback_data='popol')
kpodp = InlineKeyboardButton('Купить подписку', callback_data='kyp')
deletew = InlineKeyboardButton('Удалить🗑', callback_data='delete')
prof = InlineKeyboardMarkup().row(popol,kpodp).add(deletew)
###########о боте для админов#####
inline_keyboard = types.InlineKeyboardMarkup()
show = InlineKeyboardButton('Показать меню инфо', callback_data='show')
deletef = InlineKeyboardButton('Удалить🗑', callback_data='delete')
fagadm = InlineKeyboardMarkup().add(show).add(deletef)
##########варианты подписки#######
buyday = InlineKeyboardButton('День (30₽)', callback_data='buyday')
buyweek = InlineKeyboardButton('Неделя (200₽)', callback_data='buyweek')
buymou = InlineKeyboardButton('Месяц (500₽)', callback_data='buymou')
buymou2 = InlineKeyboardButton('2 месца (1000₽)', callback_data='buymou2')
buymou6 = InlineKeyboardButton('Пол года (2500₽)', callback_data='buymou6')
buyall = InlineKeyboardButton('Навсегда (5000₽)', callback_data='buyall')
deleteb = InlineKeyboardButton('Удалить🗑', callback_data='delete')
buy = InlineKeyboardMarkup().row(buyday,buyweek).row(buymou,buymou2).row(buymou6,buyall).add(deleteb)
###########суммы пополнения########
pop10 = InlineKeyboardButton('10', callback_data='p10')
pop30 = InlineKeyboardButton('30', callback_data='p30')
pop50 = InlineKeyboardButton('50', callback_data='p50')
pop60 = InlineKeyboardButton('60', callback_data='p60')
pop100 = InlineKeyboardButton('100', callback_data='p100')
pop150 = InlineKeyboardButton('150', callback_data='p150')
pop200 = InlineKeyboardButton('200', callback_data='p200')
pop300 = InlineKeyboardButton('300', callback_data='p300')
pop500 = InlineKeyboardButton('500', callback_data='p500')
pop700 = InlineKeyboardButton('700', callback_data='p700')
pop1000 = InlineKeyboardButton('1000', callback_data='p1000')
pop2000 = InlineKeyboardButton('2000', callback_data='p2000')
deletep = InlineKeyboardButton('Удалить🗑', callback_data='delete')
pay = InlineKeyboardMarkup().row(pop10,pop30,pop50,pop60).row(pop100,pop150,pop200,pop300).row(pop500,pop700,pop1000,pop2000).add(deletep)
###########удалить#######
delete = InlineKeyboardButton('Удалить🗑', callback_data='delete')
delete = InlineKeyboardMarkup().add(delete)