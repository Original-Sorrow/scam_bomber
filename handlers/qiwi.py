from misc import bot, dp, conn, cursor
from .functions import *
import requests
from multiprocessing import Process, Queue
from aiogram import executor, types
from aiogram.utils.helper import Helper, HelperMode, ListItem
import os
import json
from config import * #именно в конфиге находяться все данные киви
import random
import time
from time import gmtime
from time import strftime
import handlers.keyboard as kb
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

@dp.callback_query_handler(lambda c: c.data == "p10")
async def popol(callback_query: types.CallbackQuery):
    amount = 10
    user = callback_query.from_user
    comment = ''.join(random.choices('qwertyuiopsdfghjkl;zxcvbnm',k=10)) + str(random.randint(1, 1000))
    s = requests.Session()
    s.headers['authorization'] = 'Bearer' + token
    parameters = {'publicKey':publick_key,'amount':amount,'phone':phone,'comment':comment}
    h = s.get('https://oplata.qiwi.com/create', params = parameters)
    inlinepay_keyboard = types.InlineKeyboardMarkup()
    pay_sub = types.InlineKeyboardButton('Пополнить баланс(qiwi)', url=h.url)
    check_pay = types.InlineKeyboardButton(text='Проверить оплату QIWI😎',callback_data='checkpay10')
    inlinepay_keyboard = inlinepay_keyboard.add(pay_sub).add(check_pay)
    await bot.send_message(user.id, f'Для оплаты нажмите на кнопку ниже.', reply_markup=inlinepay_keyboard)
    new_payment(user.id,comment,amount)


@dp.callback_query_handler(lambda c: c.data == "checkpay10")
async def popol(callback_query: types.CallbackQuery):
    user = callback_query.from_user
    amount = 10
    comment = get_comment(user.id)
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' +  token
    parameters = {'rows': '50', 'operation':'IN'}
    h = s.get('https://edge.qiwi.com/payment-history/v1/persons/'+ phone +'/payments', params = parameters)
    result = json.loads(h.text)
    for i in range(len(result['data'])):
        if result['data'][i]['comment'] == str(comment):
            if result['data'][i]['sum']['amount'] >= amount:
                user = callback_query.from_user
                bal = cursor.execute("SELECT balance FROM users WHERE id=?", (user.id,)).fetchall()
                dbal = f"{int(bal[0][0])}"
                snyato = int(dbal)+ int(amount)
                cursor.execute(f'UPDATE users SET balance=? WHERE id=?', (snyato, user.id,))
                await bot.send_message(user.id,f'Оплата прошла, баланс пополнен на {amount}₽')
                break
        else:
            await bot.send_message(user.id, 'Не нашел вашу оплату')
            break
######### 30           
@dp.callback_query_handler(lambda c: c.data == "p30")
async def popol(callback_query: types.CallbackQuery):
    amount = 30
    user = callback_query.from_user
    comment = ''.join(random.choices('qwertyuiopsdfghjkl;zxcvbnm',k=10)) + str(random.randint(1, 1000))
    s = requests.Session()
    s.headers['authorization'] = 'Bearer' + token
    parameters = {'publicKey':publick_key,'amount':amount,'phone':phone,'comment':comment}
    h = s.get('https://oplata.qiwi.com/create', params = parameters)
    inlinepay_keyboard = types.InlineKeyboardMarkup()
    pay_sub = types.InlineKeyboardButton('Пополнить баланс(qiwi)', url=h.url)
    check_pay = types.InlineKeyboardButton(text='Проверить оплату QIWI😎',callback_data='checkpay30')
    inlinepay_keyboard = inlinepay_keyboard.add(pay_sub).add(check_pay)
    await bot.send_message(user.id, f'Для оплаты нажмите на кнопку ниже.', reply_markup=inlinepay_keyboard)
    new_payment(user.id,comment,amount)


@dp.callback_query_handler(lambda c: c.data == "checkpay30")
async def popol(callback_query: types.CallbackQuery):
    user = callback_query.from_user
    amount = 30
    comment = get_comment(user.id)
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' +  token
    parameters = {'rows': '50', 'operation':'IN'}
    h = s.get('https://edge.qiwi.com/payment-history/v1/persons/'+ phone +'/payments', params = parameters)
    result = json.loads(h.text)
    for i in range(len(result['data'])):
        if result['data'][i]['comment'] == str(comment):
            if result['data'][i]['sum']['amount'] >= amount:
                user = callback_query.from_user
                bal = cursor.execute("SELECT balance FROM users WHERE id=?", (user.id,)).fetchall()
                dbal = f"{int(bal[0][0])}"
                snyato = int(dbal)+ int(amount)
                cursor.execute(f'UPDATE users SET balance=? WHERE id=?', (snyato, user.id,))
                await bot.send_message(user.id,f'Оплата прошла, баланс пополнен на {amount}₽')
                break
        else:
            await bot.send_message(user.id, 'Не нашел вашу оплату')
            break
########50            
@dp.callback_query_handler(lambda c: c.data == "p50")
async def popol(callback_query: types.CallbackQuery):
    amount = 50
    user = callback_query.from_user
    comment = ''.join(random.choices('qwertyuiopsdfghjkl;zxcvbnm',k=10)) + str(random.randint(1, 1000))
    s = requests.Session()
    s.headers['authorization'] = 'Bearer' + token
    parameters = {'publicKey':publick_key,'amount':amount,'phone':phone,'comment':comment}
    h = s.get('https://oplata.qiwi.com/create', params = parameters)
    inlinepay_keyboard = types.InlineKeyboardMarkup()
    pay_sub = types.InlineKeyboardButton('Пополнить баланс(qiwi)', url=h.url)
    check_pay = types.InlineKeyboardButton(text='Проверить оплату QIWI😎',callback_data='checkpay50')
    inlinepay_keyboard = inlinepay_keyboard.add(pay_sub).add(check_pay)
    await bot.send_message(user.id, f'Для оплаты нажмите на кнопку ниже.', reply_markup=inlinepay_keyboard)
    new_payment(user.id,comment,amount)


@dp.callback_query_handler(lambda c: c.data == "checkpay50")
async def popol(callback_query: types.CallbackQuery):
    user = callback_query.from_user
    amount = 50
    comment = get_comment(user.id)
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' +  token
    parameters = {'rows': '50', 'operation':'IN'}
    h = s.get('https://edge.qiwi.com/payment-history/v1/persons/'+ phone +'/payments', params = parameters)
    result = json.loads(h.text)
    for i in range(len(result['data'])):
        if result['data'][i]['comment'] == str(comment):
            if result['data'][i]['sum']['amount'] >= amount:
                user = callback_query.from_user
                bal = cursor.execute("SELECT balance FROM users WHERE id=?", (user.id,)).fetchall()
                dbal = f"{int(bal[0][0])}"
                snyato = int(dbal)+ int(amount)
                cursor.execute(f'UPDATE users SET balance=? WHERE id=?', (snyato, user.id,))
                await bot.send_message(user.id,f'Оплата прошла, баланс пополнен на {amount}₽')
                break
        else:
            await bot.send_message(user.id, 'Не нашел вашу оплату')
            break
#######60            
@dp.callback_query_handler(lambda c: c.data == "p60")
async def popol(callback_query: types.CallbackQuery):
    amount = 60
    user = callback_query.from_user
    comment = ''.join(random.choices('qwertyuiopsdfghjkl;zxcvbnm',k=10)) + str(random.randint(1, 1000))
    s = requests.Session()
    s.headers['authorization'] = 'Bearer' + token
    parameters = {'publicKey':publick_key,'amount':amount,'phone':phone,'comment':comment}
    h = s.get('https://oplata.qiwi.com/create', params = parameters)
    inlinepay_keyboard = types.InlineKeyboardMarkup()
    pay_sub = types.InlineKeyboardButton('Пополнить баланс(qiwi)', url=h.url)
    check_pay = types.InlineKeyboardButton(text='Проверить оплату QIWI😎',callback_data='checkpay60')
    inlinepay_keyboard = inlinepay_keyboard.add(pay_sub).add(check_pay)
    await bot.send_message(user.id, f'Для оплаты нажмите на кнопку ниже.', reply_markup=inlinepay_keyboard)
    new_payment(user.id,comment,amount)


@dp.callback_query_handler(lambda c: c.data == "checkpay60")
async def popol(callback_query: types.CallbackQuery):
    user = callback_query.from_user
    amount = 60
    comment = get_comment(user.id)
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' +  token
    parameters = {'rows': '50', 'operation':'IN'}
    h = s.get('https://edge.qiwi.com/payment-history/v1/persons/'+ phone +'/payments', params = parameters)
    result = json.loads(h.text)
    for i in range(len(result['data'])):
        if result['data'][i]['comment'] == str(comment):
            if result['data'][i]['sum']['amount'] >= amount:
                user = callback_query.from_user
                bal = cursor.execute("SELECT balance FROM users WHERE id=?", (user.id,)).fetchall()
                dbal = f"{int(bal[0][0])}"
                snyato = int(dbal)+ int(amount)
                cursor.execute(f'UPDATE users SET balance=? WHERE id=?', (snyato, user.id,))
                await bot.send_message(user.id,f'Оплата прошла, баланс пополнен на {amount}₽')
                break
        else:
            await bot.send_message(user.id, 'Не нашел вашу оплату')
            break
########100            
@dp.callback_query_handler(lambda c: c.data == "p100")
async def popol(callback_query: types.CallbackQuery):
    amount = 100
    user = callback_query.from_user
    comment = ''.join(random.choices('qwertyuiopsdfghjkl;zxcvbnm',k=10)) + str(random.randint(1, 1000))
    s = requests.Session()
    s.headers['authorization'] = 'Bearer' + token
    parameters = {'publicKey':publick_key,'amount':amount,'phone':phone,'comment':comment}
    h = s.get('https://oplata.qiwi.com/create', params = parameters)
    inlinepay_keyboard = types.InlineKeyboardMarkup()
    pay_sub = types.InlineKeyboardButton('Пополнить баланс(qiwi)', url=h.url)
    check_pay = types.InlineKeyboardButton(text='Проверить оплату QIWI😎',callback_data='checkpay100')
    inlinepay_keyboard = inlinepay_keyboard.add(pay_sub).add(check_pay)
    await bot.send_message(user.id, f'Для оплаты нажмите на кнопку ниже.', reply_markup=inlinepay_keyboard)
    new_payment(user.id,comment,amount)

@dp.callback_query_handler(lambda c: c.data == "checkpay100")
async def popol(callback_query: types.CallbackQuery):
    user = callback_query.from_user
    amount = 100
    comment = get_comment(user.id)
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' +  token
    parameters = {'rows': '50', 'operation':'IN'}
    h = s.get('https://edge.qiwi.com/payment-history/v1/persons/'+ phone +'/payments', params = parameters)
    result = json.loads(h.text)
    for i in range(len(result['data'])):
        if result['data'][i]['comment'] == str(comment):
            if result['data'][i]['sum']['amount'] >= amount:
                user = callback_query.from_user
                bal = cursor.execute("SELECT balance FROM users WHERE id=?", (user.id,)).fetchall()
                dbal = f"{int(bal[0][0])}"
                snyato = int(dbal)+ int(amount)
                cursor.execute(f'UPDATE users SET balance=? WHERE id=?', (snyato, user.id,))
                await bot.send_message(user.id,f'Оплата прошла, баланс пополнен на {amount}₽')
                break
        else:
            await bot.send_message(user.id, 'Не нашел вашу оплату')
            break
########150            
@dp.callback_query_handler(lambda c: c.data == "p150")
async def popol(callback_query: types.CallbackQuery):
    amount = 150
    user = callback_query.from_user
    comment = ''.join(random.choices('qwertyuiopsdfghjkl;zxcvbnm',k=10)) + str(random.randint(1, 1000))
    s = requests.Session()
    s.headers['authorization'] = 'Bearer' + token
    parameters = {'publicKey':publick_key,'amount':amount,'phone':phone,'comment':comment}
    h = s.get('https://oplata.qiwi.com/create', params = parameters)
    inlinepay_keyboard = types.InlineKeyboardMarkup()
    pay_sub = types.InlineKeyboardButton('Пополнить баланс(qiwi)', url=h.url)
    check_pay = types.InlineKeyboardButton(text='Проверить оплату QIWI😎',callback_data='checkpay150')
    inlinepay_keyboard = inlinepay_keyboard.add(pay_sub).add(check_pay)
    await bot.send_message(user.id, f'Для оплаты нажмите на кнопку ниже.', reply_markup=inlinepay_keyboard)
    new_payment(user.id,comment,amount)


@dp.callback_query_handler(lambda c: c.data == "checkpay150")
async def popol(callback_query: types.CallbackQuery):
    user = callback_query.from_user
    amount = 150
    comment = get_comment(user.id)
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' +  token
    parameters = {'rows': '50', 'operation':'IN'}
    h = s.get('https://edge.qiwi.com/payment-history/v1/persons/'+ phone +'/payments', params = parameters)
    result = json.loads(h.text)
    for i in range(len(result['data'])):
        if result['data'][i]['comment'] == str(comment):
            if result['data'][i]['sum']['amount'] >= amount:
                user = callback_query.from_user
                bal = cursor.execute("SELECT balance FROM users WHERE id=?", (user.id,)).fetchall()
                dbal = f"{int(bal[0][0])}"
                snyato = int(dbal)+ int(amount)
                cursor.execute(f'UPDATE users SET balance=? WHERE id=?', (snyato, user.id,))
                await bot.send_message(user.id,f'Оплата прошла, баланс пополнен на {amount}₽')
                break
        else:
            await bot.send_message(user.id, 'Не нашел вашу оплату')
            break
##########200            
@dp.callback_query_handler(lambda c: c.data == "p200")
async def popol(callback_query: types.CallbackQuery):
    amount = 200
    user = callback_query.from_user
    comment = ''.join(random.choices('qwertyuiopsdfghjkl;zxcvbnm',k=10)) + str(random.randint(1, 1000))
    s = requests.Session()
    s.headers['authorization'] = 'Bearer' + token
    parameters = {'publicKey':publick_key,'amount':amount,'phone':phone,'comment':comment}
    h = s.get('https://oplata.qiwi.com/create', params = parameters)
    inlinepay_keyboard = types.InlineKeyboardMarkup()
    pay_sub = types.InlineKeyboardButton('Пополнить баланс(qiwi)', url=h.url)
    check_pay = types.InlineKeyboardButton(text='Проверить оплату QIWI😎',callback_data='checkpay200')
    inlinepay_keyboard = inlinepay_keyboard.add(pay_sub).add(check_pay)
    await bot.send_message(user.id, f'Для оплаты нажмите на кнопку ниже.', reply_markup=inlinepay_keyboard)
    new_payment(user.id,comment,amount)


@dp.callback_query_handler(lambda c: c.data == "checkpay200")
async def popol(callback_query: types.CallbackQuery):
    user = callback_query.from_user
    amount = 200
    comment = get_comment(user.id)
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' +  token
    parameters = {'rows': '50', 'operation':'IN'}
    h = s.get('https://edge.qiwi.com/payment-history/v1/persons/'+ phone +'/payments', params = parameters)
    result = json.loads(h.text)
    for i in range(len(result['data'])):
        if result['data'][i]['comment'] == str(comment):
            if result['data'][i]['sum']['amount'] >= amount:
                user = callback_query.from_user
                bal = cursor.execute("SELECT balance FROM users WHERE id=?", (user.id,)).fetchall()
                dbal = f"{int(bal[0][0])}"
                snyato = int(dbal)+ int(amount)
                cursor.execute(f'UPDATE users SET balance=? WHERE id=?', (snyato, user.id,))
                await bot.send_message(user.id,f'Оплата прошла, баланс пополнен на {amount}₽')
                break
        else:
            await bot.send_message(user.id, 'Не нашел вашу оплату')
            break
########300            
@dp.callback_query_handler(lambda c: c.data == "p300")
async def popol(callback_query: types.CallbackQuery):
    amount = 300
    user = callback_query.from_user
    comment = ''.join(random.choices('qwertyuiopsdfghjkl;zxcvbnm',k=10)) + str(random.randint(1, 1000))
    s = requests.Session()
    s.headers['authorization'] = 'Bearer' + token
    parameters = {'publicKey':publick_key,'amount':amount,'phone':phone,'comment':comment}
    h = s.get('https://oplata.qiwi.com/create', params = parameters)
    inlinepay_keyboard = types.InlineKeyboardMarkup()
    pay_sub = types.InlineKeyboardButton('Пополнить баланс(qiwi)', url=h.url)
    check_pay = types.InlineKeyboardButton(text='Проверить оплату QIWI😎',callback_data='checkpay300')
    inlinepay_keyboard = inlinepay_keyboard.add(pay_sub).add(check_pay)
    await bot.send_message(user.id, f'Для оплаты нажмите на кнопку ниже.', reply_markup=inlinepay_keyboard)
    new_payment(user.id,comment,amount)


@dp.callback_query_handler(lambda c: c.data == "checkpay300")
async def popol(callback_query: types.CallbackQuery):
    user = callback_query.from_user
    amount = 300
    comment = get_comment(user.id)
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' +  token
    parameters = {'rows': '50', 'operation':'IN'}
    h = s.get('https://edge.qiwi.com/payment-history/v1/persons/'+ phone +'/payments', params = parameters)
    result = json.loads(h.text)
    for i in range(len(result['data'])):
        if result['data'][i]['comment'] == str(comment):
            if result['data'][i]['sum']['amount'] >= amount:
                user = callback_query.from_user
                bal = cursor.execute("SELECT balance FROM users WHERE id=?", (user.id,)).fetchall()
                dbal = f"{int(bal[0][0])}"
                snyato = int(dbal)+ int(amount)
                cursor.execute(f'UPDATE users SET balance=? WHERE id=?', (snyato, user.id,))
                await bot.send_message(user.id,f'Оплата прошла, баланс пополнен на {amount}₽')
                break
        else:
            await bot.send_message(user.id, 'Не нашел вашу оплату')
            break
#######500            
@dp.callback_query_handler(lambda c: c.data == "p500")
async def popol(callback_query: types.CallbackQuery):
    amount = 500
    user = callback_query.from_user
    comment = ''.join(random.choices('qwertyuiopsdfghjkl;zxcvbnm',k=10)) + str(random.randint(1, 1000))
    s = requests.Session()
    s.headers['authorization'] = 'Bearer' + token
    parameters = {'publicKey':publick_key,'amount':amount,'phone':phone,'comment':comment}
    h = s.get('https://oplata.qiwi.com/create', params = parameters)
    inlinepay_keyboard = types.InlineKeyboardMarkup()
    pay_sub = types.InlineKeyboardButton('Пополнить баланс(qiwi)', url=h.url)
    check_pay = types.InlineKeyboardButton(text='Проверить оплату QIWI😎',callback_data='checkpay500')
    inlinepay_keyboard = inlinepay_keyboard.add(pay_sub).add(check_pay)
    await bot.send_message(user.id, f'Для оплаты нажмите на кнопку ниже.', reply_markup=inlinepay_keyboard)
    new_payment(user.id,comment,amount)


@dp.callback_query_handler(lambda c: c.data == "checkpay500")
async def popol(callback_query: types.CallbackQuery):
    user = callback_query.from_user
    amount = 500
    comment = get_comment(user.id)
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' +  token
    parameters = {'rows': '50', 'operation':'IN'}
    h = s.get('https://edge.qiwi.com/payment-history/v1/persons/'+ phone +'/payments', params = parameters)
    result = json.loads(h.text)
    for i in range(len(result['data'])):
        if result['data'][i]['comment'] == str(comment):
            if result['data'][i]['sum']['amount'] >= amount:
                user = callback_query.from_user
                bal = cursor.execute("SELECT balance FROM users WHERE id=?", (user.id,)).fetchall()
                dbal = f"{int(bal[0][0])}"
                snyato = int(dbal)+ int(amount)
                cursor.execute(f'UPDATE users SET balance=? WHERE id=?', (snyato, user.id,))
                await bot.send_message(user.id,f'Оплата прошла, баланс пополнен на {amount}₽')
                break
        else:
            await bot.send_message(user.id, 'Не нашел вашу оплату')
            break 
  ######700         
@dp.callback_query_handler(lambda c: c.data == "p700")
async def popol(callback_query: types.CallbackQuery):
    amount = 700
    user = callback_query.from_user
    comment = ''.join(random.choices('qwertyuiopsdfghjkl;zxcvbnm',k=10)) + str(random.randint(1, 1000))
    s = requests.Session()
    s.headers['authorization'] = 'Bearer' + token
    parameters = {'publicKey':publick_key,'amount':amount,'phone':phone,'comment':comment}
    h = s.get('https://oplata.qiwi.com/create', params = parameters)
    inlinepay_keyboard = types.InlineKeyboardMarkup()
    pay_sub = types.InlineKeyboardButton('Пополнить баланс(qiwi)', url=h.url)
    check_pay = types.InlineKeyboardButton(text='Проверить оплату QIWI😎',callback_data='checkpay700')
    inlinepay_keyboard = inlinepay_keyboard.add(pay_sub).add(check_pay)
    await bot.send_message(user.id, f'Для оплаты нажмите на кнопку ниже.', reply_markup=inlinepay_keyboard)
    new_payment(user.id,comment,amount)


@dp.callback_query_handler(lambda c: c.data == "checkpay700")
async def popol(callback_query: types.CallbackQuery):
    user = callback_query.from_user
    amount = 700
    comment = get_comment(user.id)
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' +  token
    parameters = {'rows': '50', 'operation':'IN'}
    h = s.get('https://edge.qiwi.com/payment-history/v1/persons/'+ phone +'/payments', params = parameters)
    result = json.loads(h.text)
    for i in range(len(result['data'])):
        if result['data'][i]['comment'] == str(comment):
            if result['data'][i]['sum']['amount'] >= amount:
                user = callback_query.from_user
                bal = cursor.execute("SELECT balance FROM users WHERE id=?", (user.id,)).fetchall()
                dbal = f"{int(bal[0][0])}"
                snyato = int(dbal)+ int(amount)
                cursor.execute(f'UPDATE users SET balance=? WHERE id=?', (snyato, user.id,))
                await bot.send_message(user.id,f'Оплата прошла, баланс пополнен на {amount}₽')
                break
        else:
            await bot.send_message(user.id, 'Не нашел вашу оплату')
            break
#1000            
@dp.callback_query_handler(lambda c: c.data == "p1000")
async def popol(callback_query: types.CallbackQuery):
    amount = 1000
    user = callback_query.from_user
    comment = ''.join(random.choices('qwertyuiopsdfghjkl;zxcvbnm',k=10)) + str(random.randint(1, 1000))
    s = requests.Session()
    s.headers['authorization'] = 'Bearer' + token
    parameters = {'publicKey':publick_key,'amount':amount,'phone':phone,'comment':comment}
    h = s.get('https://oplata.qiwi.com/create', params = parameters)
    inlinepay_keyboard = types.InlineKeyboardMarkup()
    pay_sub = types.InlineKeyboardButton('Пополнить баланс(qiwi)', url=h.url)
    check_pay = types.InlineKeyboardButton(text='Проверить оплату QIWI😎',callback_data='checkpay1000')
    inlinepay_keyboard = inlinepay_keyboard.add(pay_sub).add(check_pay)
    await bot.send_message(user.id, f'Для оплаты нажмите на кнопку ниже.', reply_markup=inlinepay_keyboard)
    new_payment(user.id,comment,amount)


@dp.callback_query_handler(lambda c: c.data == "checkpay1000")
async def popol(callback_query: types.CallbackQuery):
    user = callback_query.from_user
    amount = 1000
    comment = get_comment(user.id)
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' +  token
    parameters = {'rows': '50', 'operation':'IN'}
    h = s.get('https://edge.qiwi.com/payment-history/v1/persons/'+ phone +'/payments', params = parameters)
    result = json.loads(h.text)
    for i in range(len(result['data'])):
        if result['data'][i]['comment'] == str(comment):
            if result['data'][i]['sum']['amount'] >= amount:
                user = callback_query.from_user
                bal = cursor.execute("SELECT balance FROM users WHERE id=?", (user.id,)).fetchall()
                dbal = f"{int(bal[0][0])}"
                snyato = int(dbal)+ int(amount)
                cursor.execute(f'UPDATE users SET balance=? WHERE id=?', (snyato, user.id,))
                await bot.send_message(user.id,f'Оплата прошла, баланс пополнен на {amount}₽')
                break
        else:
            await bot.send_message(user.id, 'Не нашел вашу оплату')
            break
#2000
@dp.callback_query_handler(lambda c: c.data == "p2000")
async def popol(callback_query: types.CallbackQuery):
    amount = 2000
    user = callback_query.from_user
    comment = ''.join(random.choices('qwertyuiopsdfghjkl;zxcvbnm',k=10)) + str(random.randint(1, 1000))
    s = requests.Session()
    s.headers['authorization'] = 'Bearer' + token
    parameters = {'publicKey':publick_key,'amount':amount,'phone':phone,'comment':comment}
    h = s.get('https://oplata.qiwi.com/create', params = parameters)
    inlinepay_keyboard = types.InlineKeyboardMarkup()
    pay_sub = types.InlineKeyboardButton('Пополнить баланс(qiwi)', url=h.url)
    check_pay = types.InlineKeyboardButton(text='Проверить оплату QIWI😎',callback_data='checkpay2000')
    inlinepay_keyboard = inlinepay_keyboard.add(pay_sub).add(check_pay)
    await bot.send_message(user.id, f'Для оплаты нажмите на кнопку ниже.', reply_markup=inlinepay_keyboard)
    new_payment(user.id,comment,amount)


@dp.callback_query_handler(lambda c: c.data == "checkpay2000")
async def popol(callback_query: types.CallbackQuery):
    user = callback_query.from_user
    amount = 2000
    comment = get_comment(user.id)
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' +  token
    parameters = {'rows': '50', 'operation':'IN'}
    h = s.get('https://edge.qiwi.com/payment-history/v1/persons/'+ phone +'/payments', params = parameters)
    result = json.loads(h.text)
    for i in range(len(result['data'])):
        if result['data'][i]['comment'] == str(comment):
            if result['data'][i]['sum']['amount'] >= amount:
                user = callback_query.from_user
                bal = cursor.execute("SELECT balance FROM users WHERE id=?", (user.id,)).fetchall()
                dbal = f"{int(bal[0][0])}"
                snyato = int(dbal)+ int(amount)
                cursor.execute(f'UPDATE users SET balance=? WHERE id=?', (snyato, user.id,))
                await bot.send_message(user.id,f'Оплата прошла, баланс пополнен на {amount}₽')
                break
        else:
            await bot.send_message(user.id, 'Не нашел вашу оплату')
            break                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        