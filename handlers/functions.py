from misc import bot, dp, conn, cursor
from aiogram.types import Message
from aiogram import types
import time
import datetime

#получение инфы о любом столбике в бд
async def get_rang(message: types.Message):
    user = message.from_user
    cursor.execute("SELECT * FROM users WHERE id=?", (user.id,))
    data = cursor.fetchone()
    return data
#занесение в бд    
def new_user(telegram_id):
    query = f"""SELECT * from users WHERE id={telegram_id}"""
    cursor.execute(query)
    check = cursor.fetchall()
    if check:
        pass
    else:
        cursor.execute("""INSERT INTO users
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (telegram_id, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0)
                       )
        conn.commit()
        return 'new user'
#получение баланса             
async def get_balance(message: types.Message):
    try:
        user = message.from_user
        get = cursor.execute("SELECT balance FROM users WHERE id=?", (user.id,)).fetchall()
        balance = f"{str(get[0][0])}"
        return balance
    except: pass
#получение инфы активна ли подписка                    
async def get_podp(message: types.Message):
    try:
        user = message.from_user
        get = cursor.execute("SELECT podpiska FROM users WHERE id=?", (user.id,)).fetchall()
        podpiska = f"{str(get[0][0])}"
        return podpiska
    except: pass                                                         
#получаем количество юзеров                                                                         
async def get_len_users(message: types.Message):
    users = cursor.execute("SELECT id FROM users").fetchall()
    allusers = len(users)

    return allusers                                                      
#получаем количество юзеров с подпиской
async def get_len_podp(message: types.Message):
    upodp = cursor.execute("SELECT id FROM users WHERE podpiska=?", (1,)).fetchall()
    allpodp = len(upodp)
    return allpodp                                                                                                                                                       
#чекаем статус платежа
def new_payment(telegram_id, coment, payment_sum):
    cursor.execute(f'UPDATE users SET coment = ? WHERE id = ?;', (coment, telegram_id))
    cursor.execute(f'UPDATE users SET payment_sum = ? WHERE id = ?;', (payment_sum, telegram_id))
    conn.commit() 
#пополняем баланс
def add_bal(telegram_id):
    cursor.execute(f'UPDATE users SET balance = ? WHERE id = ?;', (amount, telegram_id))
    conn.commit()
#получаем  комент для пополнения киви                                                                       
def get_comment(telegram_id):
    for row in cursor.execute("SELECT id,coment FROM users"):
        user_id = row[0]
        if user_id == telegram_id:
            comment = row[1]
            return comment 
            
		
def get_sub_status(message: types.Message):
	user = message.from_user
	result = cursor.execute("SELECT podp_time FROM users WHERE id = ?", (user.id,)).fetchall()
	for row in result:
		podp_time = int(row[0])
	if podp_time < int(time.time()):
		return False
	else:
		return True 

def get_time_sub(telegram_id):
	result = cursor.execute(f'SELECT podp_time FROM users WHERE id = ?', (user.id,)).fetchall()
	for row in result:
		podp_time = int(row[0]) 
	return podp_time

def time_sub(get_time_sub):
	time_now = int(time.time())
	middle_time = int(get_time_sub) - time_now
	if middle_time > 0:
		dt = str(datetime.timedelta(seconds = middle_time))
		return dt		                                                                                                                                                                                                    