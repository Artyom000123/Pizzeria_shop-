
import random
import sqlite3

#Курсор (sql) и блок кода с заполнением базы данными, должны быть в одной функции 

db = sqlite3.connect('pizza_shops.db')#Создаём базу данных которая называется pizza_shops и подключаемся к ней
sql = db.cursor()#

#Создаём таблицу users если она не созданна (IF NOT EXISTS), со столбцами: number, name, surname...
sql.execute("""CREATE TABLE IF NOT EXISTS users (
    number INT,
    name  TEXT,
    surname  TEXT,
    username  TEXT,
    id  INT,
    status  INT,
    address01  TEXT,
    address02  TEXT,
    address03  TEXT    
    )""")
db.commit()#Потверждаем наше действие


#id1 = random.randint(1000,10000)
id1 = 1

#Функция которая записывает пользователя в базу данных
def h (name1, surname1,username1, id1, status1, address1, address2, address3 ):
    number1 = 0#
    db = sqlite3.connect('pizza_shops.db')
    sql = db.cursor()#Создаём переменную sql хронящюю в себе cursor



    



    #Щётчик для того чтобы номера в базе шли друг за другом
    while True:
        sql.execute(f"SELECT number FROM users WHERE number = '{number1}'")#Берём номер для проверки его уникальности

        if sql.fetchone() is None:#Если такого номер ещё нет то
            break#Останавливаем цикл и идём записывать

        else:#Иначе, тоесть если такой номер уже есть то
            number1 = number1 + 1#Меняем номер и проверяем ещё раз

    

    #Проверка уникальности id
    while True:    
        sql.execute(f"SELECT id FROM users WHERE id = '{id1}'")#Беррём id для проверки уникальности
        
        if sql.fetchone() is None:#Если такого id ешё нет
            
            break#Останавливаем цикл и идём записывать данные
            
        #Если такой id уже есть, прибавляем ему 1 и снова проверяем его наличие и так по кругу
        else:
            id1 = id1 + 1
    
        
      
    #Проверка уникальности username
    sql.execute(f"SELECT username FROM users WHERE username = '{username1}'")#Беррём анекдот для проверки уникальности

    if sql.fetchone() is None:#Если такого пользователя ешё нет

        
    
        
        sql.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (number1, name1, surname1, username1, id1, status1, address1, address2, address3 ))#Заливаем в таблицу информацию
        db.commit()#Потверждаем наше действие
        
    #Если такой пользователь уже есть в базе  
    else:
        sql.execute(f"UPDATE users SET status = '{status1}' WHERE username = '{username1}'")#берём пользователя по username и меняем статус на активный
        db.commit()#Потверждаем наше действие
        


#Функция которая удоляет пользователя из базы данных
def f(ctatus0,username0):
    db = sqlite3.connect('pizza_shops.db')
    sql = db.cursor()#
    

    sql.execute(f"UPDATE users SET status = '{ctatus0}' WHERE username = '{username0}'")#берём пользователя по username и меняем статус на неактивный
    
    db.commit()
    
    

#Функция которая выводит базу данных
def ss():
    db = sqlite3.connect('pizza_shops.db')
    sql = db.cursor()#
    
    print('')
    
    #Выводим таблицу
    for value1 in sql.execute("SELECT * FROM users"):
        print(value1)
    print('')
    




#Функция для замены первого адреса
def change1(address_d, fox):
    db = sqlite3.connect('pizza_shops.db')
    sql = db.cursor()
    
    
    sql.execute(f"UPDATE users SET address01 = '{address_d}' WHERE username = '{fox}'")#берём пользователя по username и меняем адрес
    
    db.commit()
    
    
    
#Функция для замены второго адреса
def change2(address_d, fox):
    db = sqlite3.connect('pizza_shops.db')#Создаём базу данных которая называется 204 и подключаемся к ней
    sql = db.cursor()
    
    
    sql.execute(f"UPDATE users SET address02 = '{address_d}' WHERE username = '{fox}'")#берём пользователя по username и меняем адрес
    
    db.commit()





#Функция для замены третьего адреса
def change3(address_d, fox):
    db = sqlite3.connect('pizza_shops.db')
    sql = db.cursor()
    
    
    
    
    sql.execute(f"UPDATE users SET address03 = '{address_d}' WHERE username = '{fox}'")#берём пользователя по username и меняем адрес
    
    db.commit()
 


#Создаём переменные которые потом импортируем в бота
db = sqlite3.connect('pizza_shops.db')
sql = db.cursor()#

    
sql.execute("SELECT address01 FROM users WHERE number = 1;")
address_d1 = sql.fetchone()#

sql.execute("SELECT address02 FROM users WHERE number = 1;")
address_d2 = sql.fetchone()

sql.execute("SELECT address03 FROM users WHERE number = 1;")
address_d3 = sql.fetchone()





db_1 = sqlite3.connect('orders.db')#Создаём базу данных которая называется orders и подключаемся к ней
sql_1 = db_1.cursor()#



#Создаём таблицу spisoc если она не созданна (IF NOT EXISTS), со столбцами: products, surname, username...
sql_1.execute("""CREATE TABLE IF NOT EXISTS shopping_list (
    products  TEXT,
    surname  TEXT,
    username  TEXT,
    address  TEXT,
    timme TEXT
    )""")
db_1.commit()#Потверждаем наше действие


f2 = "'p2 = 20, ', 'p3 = 11, ', 'p5 = 100, '"
def zp(products2, surname2, username2, address2, timme2):
    db_1 = sqlite3.connect('orders.db')
    sql_1 = db_1.cursor()#


    sql_1.execute(f"INSERT INTO shopping_list VALUES (?, ?, ?, ?, ?)", (products2, surname2, username2, address2, timme2))#Заливаем в таблицу информацию
    db_1.commit()#Потверждаем наше действие



#Функция которая выводит базу данных
def ss2():
    db_1 = sqlite3.connect('orders.db')
    sql_1 = db_1.cursor()#

    
    print('')
    
    #Выводим таблицу
    for value1 in sql_1.execute("SELECT * FROM  shopping_list "):
        print(value1)
    print('')


def prints():
    print(456-847)




