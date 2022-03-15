
import telebot#Для работы с API Telegram
from telebot import types#Для работы с API Telegram
import sqlite3#Для работы с базой данных

from SimpleQIWI import *#Для работы с API QIWI
from time import sleep#Для таймера

#Импортируем данные из базы данных
from pizza_db import h, f, ss, change1, change2, change3, prints, zp, ss2
from pizza_db import id1
from pizza_db import address_d1, address_d2, address_d3

import requests#Для HTTP запросов
import json#Для преобразования из JSON в текст

from random import randint#Рандомайзер

import telegram#

import datetime#Для того чтобы узнать дату и время


user = []#

#-----------------------------------------------------------------------------------------------------------------------
bot = telebot.TeleBot('1722275762:AA3Xdgklml-zhPloB-mSYi5caktJsEs')# Token бота

mm = types.ReplyKeyboardMarkup(resize_keyboard=True)
mm2 = types.ReplyKeyboardMarkup(resize_keyboard=True)

#переменные содержащие в себе кнопки
button1 = types.KeyboardButton(" Ассортимент")
button2 = types.KeyboardButton(" зарегистрироватся")
button3 = types.KeyboardButton(" отписатся")
button4 = types.KeyboardButton(" корзина")

#Сначало появляется эта кнопка а после её нажатия остальные
mm.add(button2)
reply_markup=mm

mm2.add(button1,button3,button4)
reply_markup=mm2

#Обрабатываем команду старт
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=mm)
    

fgh= 1


suma = 0#Итоговая сумма всех покупок

p1 = 0
p2 = 0
p3 = 0

p4 = 0
p5 = 0
p6 = 0
p7 = 0
p8 = 0
p9 = 0
p10 = 0
p11 = 0
p12 = 0
p13 = 0
p14 = 0
p15 = 0
p16 = 0
p17 = 0
p18 = 0
p19 = 0
p20 = 0
p21 = 0
p22 = 0
p23 = 0
p24 = 0
p25 = 0
p26 = 0
p27 = 0
p28 = 0
p29 = 0
p30 = 0
p31 = 0
p32 = 0
p33 = 0
p34 = 0
p35 = 0
p36 = 0
p37 = 0
p38 = 0
p39 = 0
p40 = 0

su1 = 0
su2 = 0
su3 = 0
su4 = 0
su5 = 0
su6 = 0
su7 = 0
su8 = 0
su9 = 0
su10 = 0
su11 = 0
su12 = 0
su13 = 0

se1 = 0
se2 = 0
se3 = 0
se4 = 0
se5 = 0
se6 = 0
se7 = 0
se8 = 0
se9 = 0

sn1 = 0
sn2 = 0
sn3 = 0

sp1 = 0
sp2 = 0
sp3 = 0
sp4 = 0
sp5 = 0
sp6 = 0
sp7 = 0
sp8 = 0
sp9 = 0
sp10 = 0
sp11 = 0
sp12 = 0
sp13 = 0

sa1 = 0
sa2 = 0
sa3 = 0
sa4 = 0
sa5 = 0
sa6 = 0

be1 = 0
be2 = 0
be3 = 0
be4 = 0
be5 = 0
be6 = 0
be7 = 0
be8 = 0
be9 = 0
be10 = 0
be11 = 0
be12 = 0
be13 = 0

ka1 = 0
ka2 = 0
ka3 = 0
ka4 = 0

sal1 = 0
sal2 = 0
sal3 = 0





n1 = 0
n2 = 0
n3 = 0

z1 = 0
z2 = 0
z3 = 0




#____________________________________________________________________________________________________________________________________________________________________________________________

@bot.message_handler(content_types=['text'])#Говорим что будем работать с текстом
def diolog(message):
    
    mar = "Маргарита"
    fore = "Четыре сезона"
    more = "Пицца с морепродуктами"
    
    def buy ():
        bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAIZr2F768a6wQuozapKn6lzQOT0d7w1AAKNtTEbWJfgSwmb5NEVN2ZtAQADAgADeAADIQQ')
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Пицца', callback_data=1))#Это кнопки с идентификаторами
        markup.add(telebot.types.InlineKeyboardButton(text='Суши', callback_data=2))
        markup.add(telebot.types.InlineKeyboardButton(text='Сеты', callback_data=3))
        markup.add(telebot.types.InlineKeyboardButton(text='Закуски', callback_data=4))
        markup.add(telebot.types.InlineKeyboardButton(text='Спец предложения', callback_data=5))
        markup.add(telebot.types.InlineKeyboardButton(text='Соусы', callback_data=6))
        markup.add(telebot.types.InlineKeyboardButton(text='Напитки', callback_data=7))
        markup.add(telebot.types.InlineKeyboardButton(text='Кальцоне', callback_data=8))
        markup.add(telebot.types.InlineKeyboardButton(text='Салаты', callback_data=9))

        bot.send_message(message.chat.id, text="Ассортимент", reply_markup=markup)#Это текст к которому прекреплены кнопки

    #Корзина
    def products_basket (p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9, p_10, p_11, p_12, p_13, p_14, p_15, p_16, p_17, p_18, p_19, p_20, 
                        p_21, p_22, p_23, p_24, p_25, p_26, p_27, p_28 , p_29, p_30, p_31, p_32, p_33, p_34, p_35, p_36, p_37, p_38, p_39, p_40, 
                        su_1, su_2, su_3, su_4, su_5, su_6, su_7, su_8, su_9, su_10, su_11 , su_12, su_13, 
                        se_1, se_2, se_3, se_4, se_5, se_6, se_7, se_8, se_9, 
                        sn_1, sn_2, sn_3, 
                        sp_1, sp_2, sp_3, sp_4, sp_5, sp_6, sp_7, sp_8, sp_9, sp_10, sp_11, sp_12, sp_13, 
                        sa_1, sa_2, sa_3, sa_4, sa_5, 
                        be_1, be_2, be_3, be_4, be_5, be_6, be_7, be_8, be_9, be_10, be_11, be_12, be_13, 
                        ka_1, ka_2, ka_3, ka_4, 
                        sal_1, sal_2, sal_3):

        global product
        l_1 = ['Томаты и ананасы', 'Грибная', 'Семейная', 'Морская', 'NINJA Джуниор', 'Пепперони 30 см', 'Сабай 30 см', 'Чизо 30 см', 'Крэнг 30 см', 
                'Овощи Гриль 30 см', 'Крейзи Пепперони 30 см', 'Сырная 30 см', 'Аррива 30 см', 'Рафаэль 30 см', 'Принглс 30 см', 'Хот Чикен 30 см', 'Ниндзя Опята 30 см»', 
                'Цыпленок Барбекю 30 см', 'Сырный Цыпленок 30 см', 'Донателло 30 см', 'Шредер 30 см', 'Мисс Эйприл 30 см', 'Ранч 30 см', 
                'Леонардо 30 см', 'Кавабанга 30 см', 'Ниндзя Чизбургер 30 см', 'Ниндзяго 30 см', 'Четыре сыра 30 см', 'Ниндзя Италия 30 см', 
                'Сэнсэй 30 см', 'Сплинтер 30 см', 'Микеланджело 30 см','Мэри Джейн 30 см','Акуна Матата 30 см','Ниндзя Терияки 30 см','Пепперони Фреш 30 см','Мексика 30 см',
                'Сладкий Цыпа 30 см', 'Ниндзя Гавайи 30 см', 'Ягоды и пряности 30 см', 
        
                'Филадельфия с лососем', 'Филадельфия с угрем', 'Филадельфия с тунцом', 'Калифорния с лососем', 'Ролл с опалённым лососем и креветкой', 'Ролл с курицей кимчи и омлетом', 'Запеченный ролл с курицей', 'Ролл с курицей кимчи и омлетом', 'Темпура с креветкой', 'Темпура с курицей', 'Темпура с тунцом', 'Темпура с Угрем', 'Темпура с Лососем', 
                'Сет Вегетарианский', 'Сет Раф', 'Сет  Темпура', 'Сет Трио', 'Микс 2', 'Сет Кавабанга', 'Сет Нидзяго', 'Сет Запечный', 'Сет Класcический', 
                'Картофель фри', 'Наггетсы', 'Картофельные дольки', 
                'Комбо (10 пицц)', 'Комбо (3 пиццы)', 'Комбо (5 пицц)', 'Комбо (2 пиццы)', 'Комбо (7 пицц)', 'Комбо для тебя', 'Снек-комбо', 'SUPER-КОМБО', 'Комбо (2 пиццы)2', '2 вкусв', 'Трио', 'Ninja Party', '6 хит', 
                'Чесночный', 'Томатный', 'Сырный', 'Кисло-сладкий', 'Соус барбекю', 
                'Сок Rich Яблоко', 'Сок Rich Персик', 'Сок Rich Мультифрукт', 'Сок Rich Вишня', 'Сок Rich Апельсин', 'Сок Rich Ананас', 'Sprite 0.5', 'Sprite 1.0', 'Fanta 0.5', 'Fanta 1.0', 'Coca-cola 0.5', 'Coca-cola 1.0', 'Coca-cola 0.2', 
                'Кальцоне Рафаэль', 'Кальцоне Шредер', 'Кальцоне Чизбургер', 'Кальцоне Цезарь', 
                'Гавайский', 'Цезарь', 'Греческий']

        l_2 = [p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9, p_10, p_11, p_12, p_13, p_14, p_15, p_16, p_17, p_18, p_19, p_20, 
                p_21, p_22, p_23, p_24, p_25, p_26, p_27, p_28 , p_29, p_30, p_31, p_32, p_33, p_34, p_35, p_36, p_37, p_38, p_39, p_40, 
                su_1, su_2, su_3, su_4, su_5, su_6, su_7, su_8, su_9, su_10, su_11 , su_12, su_13, 
                se_1, se_2, se_3, se_4, se_5, se_6, se_7, se_8, se_9, 
                sn_1, sn_2, sn_3, 
                sp_1, sp_2, sp_3, sp_4, sp_5, sp_6, sp_7, sp_8, sp_9, sp_10, sp_11, sp_12, sp_13, 
                sa_1, sa_2, sa_3, sa_4, sa_5, 
                be_1, be_2, be_3, be_4, be_5, be_6, be_7, be_8, be_9, be_10, be_11, be_12, be_13, 
                ka_1, ka_2, ka_3, ka_4, 
                sal_1, sal_2, sal_3]

        #l_db = []
        l_kk = ''
        for a in l_2:#Количество Проходимся по товарам и определяем не равныли их количество нулю
                
            for aa in l_1:#Имя. Проходимся по именам дабы количнство товара была потписана именем товара.
                    
                if a != 0:#Проверяем не равна ли сумма 0
                    #Если сумма больше 0 то выводим имя и сумму
                    ty = f'\n{aa} = {a} шт., '
                    
                    l_kk = l_kk + ty
                    

                    l_1.pop(0)#Удаляем первый элемент спика чтобы когда цикл заново заработал он взял не снова первый элемент а уже следующий (второй)
                        
                    break#Останавливаем цикл
                        
                else :#Если сумма равна нулю то не выводим её
                    l_1.pop(0)#Удаляем первый элемент спика чтобы когда цикл заново заработал он взял не снова первый элемент а уже следующий (второй)
                    break
        
        return l_kk




    
    
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global p10
    global p11
    global p12
    global p13
    global p14
    global p15
    global p16
    global p17
    global p18
    global p19
    global p20
    global p21
    global p22
    global p23
    global p24
    global p25
    global p26
    global p27
    global p28 
    global p29
    global p30
    global p31
    global p32
    global p33
    global p34
    global p35
    global p36
    global p37
    global p38
    global p39
    global p40

    global su1
    global su2
    global su3
    global su4
    global su5
    global su6
    global su7
    global su8
    global su9
    global su10
    global su11
    global su12 
    global su13

    global se1
    global se2
    global se3
    global se4
    global se5
    global se6
    global se7
    global se8
    global se9

    global sn1
    global sn2
    global sn3

    global sp1
    global sp2
    global sp3
    global sp4
    global sp5
    global sp6
    global sp7
    global sp8
    global sp9
    global sp10
    global sp11
    global sp12
    global sp13

    global sa1
    global sa2
    global sa3
    global sa4
    global sa5
    global sa6

    global be1
    global be2
    global be3
    global be4
    global be5
    global be6
    global be7
    global be8
    global be9
    global be10
    global be11
    global be12
    global be13

    global ka1
    global ka2
    global ka3
    global ka4

    global sal1
    global sal2
    global sal3

    global n1
    global n2
    global n3
    global z1
    global z2
    global z3

    global suma
    
 

    #Это кнопки которые выскакивают в диологе если написпть определённую фразу
    if message.text.lower() == 'ассортимент':#Если мы пишем это то   
        buy()
      
        
    elif message.text.lower() == 'корзина':#Если мы пишем это то
        ssb = products_basket(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, 
                            p21, p22, p23, p24, p25, p26, p27, p28 , p29, p30, p31, p32, p33, p34, p35, p36, p37, p38, p39, p40, 
                            su1, su2, su3, su4, su5, su6, su7, su8, su9, su10, su11 , su12, su13, 
                            se1, se2, se3, se4, se5, se6, se7, se8, se9, 
                            sn1, sn2, sn3, 
                            sp1, sp2, sp3, sp4, sp5, sp6, sp7, sp8, sp9, sp10, sp11, sp12, sp13, 
                            sa1, sa2, sa3, sa4, sa5,
                            be1, be2, be3, be4, be5, be6, be7, be8, be9, be10, be11, be12, be13, 
                            ka1, ka2, ka3, ka4, 
                            sal1, sal2, sal3)#Записываем в переменную значение другой переменной внутри функции

        #Кнопки
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Купить', callback_data=0.4))
        markup.add(telebot.types.InlineKeyboardButton(text='Очистить', callback_data=0.5))
        

        bot.send_message(message.chat.id, f"""Корзина: {ssb} \nИтоговая сумма'{suma}' руб.""",reply_markup=markup)


        
      
     
            
    #Записываем человека в базу данных если его там ещё небыло, и меняем его статус если он уже был
    elif message.text.lower() == 'зарегистрироватся':#Если мы пишем это то

        if message.from_user.username == None:
            #print('У вас не настроен username, без него бот не может нормально работать, настройте его пожалуста')
            bot.send_message(message.chat.id, text='У вас не настроен username, без него бот не может нормально работать, настройте его пожалуйста')

        else:
            #h("Имя14","Фамилия14","gogi-1",id1,1,"Пусто", "Пусто", "Пусто")#Человек которого мы записываем
            h(message.from_user.first_name, message.from_user.last_name, message.from_user.username, id1, 1 ,"Пусто", "Пусто", "Пусто")
            ss()#Выводим базу данных
            bot.send_message(message.chat.id, text='Что мы можем', reply_markup=mm2)#Говорим что должны вывести кнопки находяшиеся в переменной mm2


    #Меняем статус пользователя в базе на неактивного
    elif message.text.lower() == 'отписатся':#Если мы пишем это то
        #f(0,message.from_user.username)
        f(0,message.from_user.username)#Челевек которого мы обозначаем как неактивного пользователя
        ss()#Выводим базу данных
        bot.send_message(message.chat.id, text='Что мы можем', reply_markup=mm)#Говорим что должны вывести кнопки находяшиеся в переменной mm


    else:
        bot.send_message(message.chat.id, message.text)#Бот повторяет всё что мы пишем
        
        bot.send_message(message.chat.id, text="[`Скопируй этот текст`] ", parse_mode=telegram.ParseMode.MARKDOWN)#Легко копируемый текст
        #bot.send_message(message.chat.id, text='<i>Извини я и дальше буду за тобой повторять</i>', parse_mode=telegram.ParseMode.HTML)
        #print(message.text)








#Это реакция на нажатие кнопок прикреплённых к сообщениям
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    adr1 = 'Адрес 1'
    
    #Переменные обозначают количество тех или иных продуктов в  корзтне
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global p10
    global p11
    global p12
    global p13
    global p14
    global p15
    global p16
    global p17
    global p18
    global p19
    global p20
    global p21
    global p22
    global p23
    global p24
    global p25
    global p26
    global p27
    global p28 
    global p29
    global p30
    global p31
    global p32
    global p33
    global p34
    global p35
    global p36
    global p37
    global p38
    global p39
    global p40

    global su1
    global su2
    global su3
    global su4
    global su5
    global su6
    global su7
    global su8
    global su9
    global su10
    global su11 
    global su12 
    global su13

    global se1
    global se2
    global se3
    global se4
    global se5
    global se6
    global se7
    global se8
    global se9

    global sn1
    global sn2
    global sn3

    global sp1
    global sp2
    global sp3
    global sp4
    global sp5
    global sp6
    global sp7
    global sp8
    global sp9
    global sp10
    global sp11
    global sp12
    global sp13

    global sa1
    global sa2
    global sa3
    global sa4
    global sa5
    global sa6

    global be1
    global be2
    global be3
    global be4
    global be5
    global be6
    global be7
    global be8
    global be9
    global be10
    global be11
    global be12
    global be13

    global ka1
    global ka2
    global ka3
    global ka4

    global sal1
    global sal2
    global sal3

    global n1
    global n2
    global n3
    global z1
    global z2
    global z3

    global suma

    answer = ''

    def PIZZA ():
        bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIMxmDQcLYeOmsNs-goHShuCe7SmzeKAAK2ujEbrKKASs8wUNPQ0tlWjKF_pS4AAwEAAwIAA3kAA0dnAgABHwQ')#Это фото над кнопками
        #Это кнопки с идентификаторами
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Томаты и ананасы', callback_data=1.1))#Это кнопки с идентификаторами
        markup.add(telebot.types.InlineKeyboardButton(text='Грибная', callback_data=1.2))
        markup.add(telebot.types.InlineKeyboardButton(text='Семейная', callback_data=1.3))
        markup.add(telebot.types.InlineKeyboardButton(text='Морская', callback_data=1.4))
        markup.add(telebot.types.InlineKeyboardButton(text='NINJA Джуниор', callback_data=1.5))
        markup.add(telebot.types.InlineKeyboardButton(text='Пепперони 30 см', callback_data=1.6))
        markup.add(telebot.types.InlineKeyboardButton(text='Сабай 30 см', callback_data=1.7))
        markup.add(telebot.types.InlineKeyboardButton(text='Чизо 30 см', callback_data=1.8))
        markup.add(telebot.types.InlineKeyboardButton(text='Крэнг 30 см', callback_data=1.9))
        markup.add(telebot.types.InlineKeyboardButton(text='Овощи Гриль 30 см', callback_data=110))
        markup.add(telebot.types.InlineKeyboardButton(text='Крейзи Пепперони 30 см', callback_data=1.11))
        markup.add(telebot.types.InlineKeyboardButton(text='Сырная 30 см', callback_data=1.12))
        markup.add(telebot.types.InlineKeyboardButton(text='Аррива 30 см', callback_data=1.13))
        markup.add(telebot.types.InlineKeyboardButton(text='Рафаэль 30 см', callback_data=1.14))
        markup.add(telebot.types.InlineKeyboardButton(text='Принглс 30 см', callback_data=1.15))
        markup.add(telebot.types.InlineKeyboardButton(text='Хот Чикен 30 см', callback_data=1.16))
        markup.add(telebot.types.InlineKeyboardButton(text='Ниндзя Опята 30 см»', callback_data=1.17))
        markup.add(telebot.types.InlineKeyboardButton(text='Цыпленок Барбекю 30 см', callback_data=1.18))
        markup.add(telebot.types.InlineKeyboardButton(text='Сырный Цыпленок 30 см', callback_data=1.19))
        markup.add(telebot.types.InlineKeyboardButton(text='Донателло 30 см', callback_data=120))
        markup.add(telebot.types.InlineKeyboardButton(text='Шредер 30 см', callback_data=1.21))
        markup.add(telebot.types.InlineKeyboardButton(text='Мисс Эйприл 30 см', callback_data=1.22))
        markup.add(telebot.types.InlineKeyboardButton(text='Ранч 30 см', callback_data=1.23))
        markup.add(telebot.types.InlineKeyboardButton(text='Леонардо 30 см', callback_data=1.24))
        markup.add(telebot.types.InlineKeyboardButton(text='Кавабанга 30 см', callback_data=1.25))
        markup.add(telebot.types.InlineKeyboardButton(text='Ниндзя Чизбургер 30 см', callback_data=1.26))
        markup.add(telebot.types.InlineKeyboardButton(text='Ниндзяго 30 см', callback_data=1.27))
        markup.add(telebot.types.InlineKeyboardButton(text='Четыре сыра 30 см', callback_data=1.28))
        markup.add(telebot.types.InlineKeyboardButton(text='Ниндзя Италия 30 см', callback_data=1.29))
        markup.add(telebot.types.InlineKeyboardButton(text='Сэнсэй 30 см', callback_data=130))
        markup.add(telebot.types.InlineKeyboardButton(text='Сплинтер 30 см', callback_data=1.31))
        markup.add(telebot.types.InlineKeyboardButton(text='Микеланджело 30 см', callback_data=1.32))
        markup.add(telebot.types.InlineKeyboardButton(text='Мэри Джейн 30 см', callback_data=1.33))
        markup.add(telebot.types.InlineKeyboardButton(text='Акуна Матата 30 см', callback_data=1.34))
        markup.add(telebot.types.InlineKeyboardButton(text='Ниндзя Терияки 30 см', callback_data=1.35))
        markup.add(telebot.types.InlineKeyboardButton(text='Пепперони Фреш 30 см', callback_data=1.36))
        markup.add(telebot.types.InlineKeyboardButton(text='Мексика 30 см', callback_data=1.37))
        markup.add(telebot.types.InlineKeyboardButton(text='Сладкий Цыпа 30 см', callback_data=1.38))
        markup.add(telebot.types.InlineKeyboardButton(text='Ниндзя Гавайи 30 см', callback_data=1.39))
        markup.add(telebot.types.InlineKeyboardButton(text='Ягоды и пряности 30 см', callback_data=140))
        bot.send_message(call.message.chat.id, text="Какую пиццу вы бы хотели сегодня выбрать?", reply_markup=markup)#Это текст к которому прекреплены кнопки

    
    def SUSHI ():
        bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIScGEzaUa-OIPxT6U5NsjuGzv8yDcdAALPtDEbTWWZSUheo-Tm8lFqAQADAgADeQADIAQ')
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Филадельфия с лососем', callback_data=2.1))
        markup.add(telebot.types.InlineKeyboardButton(text='Филадельфия с угрем', callback_data=2.2))
        markup.add(telebot.types.InlineKeyboardButton(text='Филадельфия с тунцом', callback_data=2.3))
        markup.add(telebot.types.InlineKeyboardButton(text='Калифорния с лососем', callback_data=2.4))
        markup.add(telebot.types.InlineKeyboardButton(text='Ролл с опалённым лососем и креветкой', callback_data=2.5))
        markup.add(telebot.types.InlineKeyboardButton(text='Ролл с курицей кимчи и омлетом', callback_data=2.6))
        markup.add(telebot.types.InlineKeyboardButton(text='Запеченный ролл с курицей', callback_data=2.7))
        markup.add(telebot.types.InlineKeyboardButton(text='Ролл с курицей кимчи и омлетом', callback_data=2.8))
        markup.add(telebot.types.InlineKeyboardButton(text='Темпура с креветкой', callback_data=2.9))
        markup.add(telebot.types.InlineKeyboardButton(text='Темпура с курицей', callback_data=210))
        markup.add(telebot.types.InlineKeyboardButton(text='Темпура с тунцом', callback_data=2.11))
        markup.add(telebot.types.InlineKeyboardButton(text='Темпура с Угрем', callback_data=2.12))
        markup.add(telebot.types.InlineKeyboardButton(text='Темпура с Лососем', callback_data=2.13))
        bot.send_message(call.message.chat.id, text="Какие суши вы предпочитаете", reply_markup=markup)


    def SETS ():
        bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIZ6mF78D-6W-fMsk_dCLz_ULjzMWbyAAKctTEbWJfgSzA1fq46oXMpAQADAgADeAADIQQ')
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Сет Вегетарианский', callback_data=3.1))
        markup.add(telebot.types.InlineKeyboardButton(text='Сет Раф', callback_data=3.2))
        markup.add(telebot.types.InlineKeyboardButton(text='Сет  Темпура', callback_data=3.3))
        markup.add(telebot.types.InlineKeyboardButton(text='Сет Трио', callback_data=3.4))
        markup.add(telebot.types.InlineKeyboardButton(text='Микс 2', callback_data=3.5))
        markup.add(telebot.types.InlineKeyboardButton(text='Сет Кавабанга', callback_data=3.6))
        markup.add(telebot.types.InlineKeyboardButton(text='Сет Нидзяго', callback_data=3.7))
        markup.add(telebot.types.InlineKeyboardButton(text='Сет Запечный', callback_data=3.8))
        markup.add(telebot.types.InlineKeyboardButton(text='Сет Класcический', callback_data=3.9))
        bot.send_message(call.message.chat.id, text="Какие сеты вы предпочитаете", reply_markup=markup)


    def SNACKS ():
        bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIMyGDQcQ7Glh9JWmBuBC4u8h03OQZ-AAK4ujEbrKKASo_r8QIuTMFcuteNoi4AAwEAAwIAA3kAA_LtAwABHwQ')
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Картофель фри', callback_data=4.1))
        markup.add(telebot.types.InlineKeyboardButton(text='Картофельные дольки', callback_data=4.2))
        markup.add(telebot.types.InlineKeyboardButton(text='Наггетсы', callback_data=4.3))
        bot.send_message(call.message.chat.id, text="Выберите закуски", reply_markup=markup)
    

    def SPECIAL_OFFERS ():
        bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIZ2GF772AGTSEJAAFruwf4d5YF3XHqBwACmbUxG1iX4Et5DUwF-sBmEgEAAwIAA3gAAyEE')
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Комбо (10 пицц)', callback_data=5.1))
        markup.add(telebot.types.InlineKeyboardButton(text='Комбо (3 пиццы)', callback_data=5.2))
        markup.add(telebot.types.InlineKeyboardButton(text='Комбо (5 пицц)', callback_data=5.3))
        markup.add(telebot.types.InlineKeyboardButton(text='Комбо (2 пиццы)', callback_data=5.4))
        markup.add(telebot.types.InlineKeyboardButton(text='Комбо (7 пицц)', callback_data=5.5))
        markup.add(telebot.types.InlineKeyboardButton(text='Комбо для тебя', callback_data=5.6))
        markup.add(telebot.types.InlineKeyboardButton(text='Снек-комбо', callback_data=5.7))
        markup.add(telebot.types.InlineKeyboardButton(text='SUPER-КОМБО', callback_data=5.8))
        markup.add(telebot.types.InlineKeyboardButton(text='Комбо (2 пиццы)2', callback_data=5.9))
        markup.add(telebot.types.InlineKeyboardButton(text='2 вкуса', callback_data=510))
        markup.add(telebot.types.InlineKeyboardButton(text='Трио', callback_data=5.11))
        markup.add(telebot.types.InlineKeyboardButton(text='Ninja Party', callback_data=5.12))
        markup.add(telebot.types.InlineKeyboardButton(text='6 хит', callback_data=5.13))
        bot.send_message(call.message.chat.id, text="Вас сегодня ждёт", reply_markup=markup)

    
    def SAUCES ():
        bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIZ1WF77nOl8IT_17Jn_sEMaSKjghhCAAKYtTEbWJfgS8lMbGaVeOeDAQADAgADeQADIQQ')
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Чесночный', callback_data=6.1))
        markup.add(telebot.types.InlineKeyboardButton(text='Томатный', callback_data=6.2))
        markup.add(telebot.types.InlineKeyboardButton(text='Сырный', callback_data=6.3))
        markup.add(telebot.types.InlineKeyboardButton(text='Кисло-сладкий', callback_data=6.4))
        markup.add(telebot.types.InlineKeyboardButton(text='Соус барбекю', callback_data=6.5))
        bot.send_message(call.message.chat.id, text="Выберите соусы", reply_markup=markup)


    def BEVERAGES ():
        bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIMx2DQcOCab_u1jRyiMca70wTw0pdmAAK3ujEbrKKASpsMP8QQPGKWsTCfqC4AAwEAAwIAA3kAA94ZAAIfBA')
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Сок Rich Яблоко', callback_data=7.1))
        markup.add(telebot.types.InlineKeyboardButton(text='Сок Rich Персик', callback_data=7.2))
        markup.add(telebot.types.InlineKeyboardButton(text='Сок Rich Мультифрукт', callback_data=7.3))
        markup.add(telebot.types.InlineKeyboardButton(text='Сок Rich Вишня', callback_data=7.4))
        markup.add(telebot.types.InlineKeyboardButton(text='Сок Rich Апельсин', callback_data=7.5))
        markup.add(telebot.types.InlineKeyboardButton(text='Сок Rich Ананас', callback_data=7.6))
        markup.add(telebot.types.InlineKeyboardButton(text='Sprite 0.5', callback_data=7.7))
        markup.add(telebot.types.InlineKeyboardButton(text='Sprite 1.0', callback_data=7.8))
        markup.add(telebot.types.InlineKeyboardButton(text='Fanta 0.5', callback_data=7.9))
        markup.add(telebot.types.InlineKeyboardButton(text='Fanta 1.0', callback_data=710))
        markup.add(telebot.types.InlineKeyboardButton(text='Coca-cola 0.5', callback_data=7.11))
        markup.add(telebot.types.InlineKeyboardButton(text='Coca-cola 1.0', callback_data=7.12))
        markup.add(telebot.types.InlineKeyboardButton(text='Coca-cola 0.2', callback_data=7.13))
        bot.send_message(call.message.chat.id, text="Выберите напиток", reply_markup=markup)


    def KALZONE ():
        bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIZwWF77MFTXMlcaYqGFFwS8ziXg6yxAAKPtTEbWJfgSzd0mLrR5965AQADAgADeAADIQQ')
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Кальцоне Рафаэль', callback_data=8.1))
        markup.add(telebot.types.InlineKeyboardButton(text='Кальцоне Шредер', callback_data=8.2))
        markup.add(telebot.types.InlineKeyboardButton(text='Кальцоне Чизбургер', callback_data=8.3))
        markup.add(telebot.types.InlineKeyboardButton(text='Кальцоне Цезарь', callback_data=8.4))
        bot.send_message(call.message.chat.id, text="Выберите кальсоне", reply_markup=markup)


    def SALADS ():
        bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIZ0GF77cUwj-LxX9hf25GZE-yMgBDrAAKUtTEbWJfgS1JAYnRc291cAQADAgADcwADIQQ')
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Гавайский', callback_data=9.1))
        markup.add(telebot.types.InlineKeyboardButton(text='Цезарь', callback_data=9.2))
        markup.add(telebot.types.InlineKeyboardButton(text='Греческий', callback_data=9.3))
        bot.send_message(call.message.chat.id, text="Выберите салат", reply_markup=markup)



    def goods_db (p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9, p_10, p_11, p_12, p_13, p_14, p_15, p_16, p_17, p_18, p_19, p_20, 
                    p_21, p_22, p_23, p_24, p_25, p_26, p_27, p_28 , p_29, p_30, p_31, p_32, p_33, p_34, p_35, p_36, p_37, p_38, p_39, p_40, 
                    su_1, su_2, su_3, su_4, su_5, su_6, su_7, su_8, su_9, su_10, su_11 , su_12, su_13, 
                    se_1, se_2, se_3, se_4, se_5, se_6, se_7, se_8, se_9, 
                    sn_1, sn_2, sn_3, 
                    sp_1, sp_2, sp_3, sp_4, sp_5, sp_6, sp_7, sp_8, sp_9, sp_10, sp_11, sp_12, sp_13, 
                    sa_1, sa_2, sa_3, sa_4, sa_5, 
                    be_1, be_2, be_3, be_4, be_5, be_6, be_7, be_8, be_9, be_10, be_11, be_12, be_13, 
                    ka_1, ka_2, ka_3, ka_4, 
                    sal_1, sal_2, sal_3, sis):

        
        #Собираем информацию о том что мы купили чтобы записать её в базу данных
        l_1 = ['Томаты и ананасы', 'Грибная', 'Семейная', 'Морская', 'NINJA Джуниор', 'Пепперони 30 см', 'Сабай 30 см', 'Чизо 30 см', 'Крэнг 30 см', 
                'Овощи Гриль 30 см', 'Крейзи Пепперони 30 см', 'Сырная 30 см', 'Аррива 30 см', 'Рафаэль 30 см', 'Принглс 30 см', 'Хот Чикен 30 см', 'Ниндзя Опята 30 см»', 
                'Цыпленок Барбекю 30 см', 'Сырный Цыпленок 30 см', 'Донателло 30 см', 'Шредер 30 см', 'Мисс Эйприл 30 см', 'Ранч 30 см', 
                'Леонардо 30 см', 'Кавабанга 30 см', 'Ниндзя Чизбургер 30 см', 'Ниндзяго 30 см', 'Четыре сыра 30 см', 'Ниндзя Италия 30 см', 
                'Сэнсэй 30 см', 'Сплинтер 30 см', 'Микеланджело 30 см','Мэри Джейн 30 см','Акуна Матата 30 см','Ниндзя Терияки 30 см','Пепперони Фреш 30 см','Мексика 30 см',
                'Сладкий Цыпа 30 см', 'Ниндзя Гавайи 30 см', 'Ягоды и пряности 30 см', 
        
                'Филадельфия с лососем', 'Филадельфия с угрем', 'Филадельфия с тунцом', 'Калифорния с лососем', 'Ролл с опалённым лососем и креветкой', 'Ролл с курицей кимчи и омлетом', 'Запеченный ролл с курицей', 'Ролл с курицей кимчи и омлетом', 'Темпура с креветкой', 'Темпура с курицей', 'Темпура с тунцом', 'Темпура с Угрем', 'Темпура с Лососем', 
                'Сет Вегетарианский', 'Сет Раф', 'Сет  Темпура', 'Сет Трио', 'Микс 2', 'Сет Кавабанга', 'Сет Нидзяго', 'Сет Запечный', 'Сет Класcический', 
                'Картофель фри', 'Наггетсы', 'Картофельные дольки', 
                'Комбо (10 пицц)', 'Комбо (3 пиццы)', 'Комбо (5 пицц)', 'Комбо (2 пиццы)', 'Комбо (7 пицц)', 'Комбо для тебя', 'Снек-комбо', 'SUPER-КОМБО', 'Комбо (2 пиццы)2', '2 вкусв', 'Трио', 'Ninja Party', '6 хит', 
                'Чесночный', 'Томатный', 'Сырный', 'Кисло-сладкий', 'Соус барбекю', 
                'Сок Rich Яблоко', 'Сок Rich Персик', 'Сок Rich Мультифрукт', 'Сок Rich Вишня', 'Сок Rich Апельсин', 'Сок Rich Ананас', 'Sprite 0.5', 'Sprite 1.0', 'Fanta 0.5', 'Fanta 1.0', 'Coca-cola 0.5', 'Coca-cola 1.0', 'Coca-cola 0.2', 
                'Кальцоне Рафаэль', 'Кальцоне Шредер', 'Кальцоне Чизбургер', 'Кальцоне Цезарь', 
                'Гавайский', 'Цезарь', 'Греческий' ]

        l_2 = [p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9, p_10, p_11, p_12, p_13, p_14, p_15, p_16, p_17, p_18, p_19, p_20, 
                p_21, p_22, p_23, p_24, p_25, p_26, p_27, p_28 , p_29, p_30, p_31, p_32, p_33, p_34, p_35, p_36, p_37, p_38, p_39, p_40, 
                su_1, su_2, su_3, su_4, su_5, su_6, su_7, su_8, su_9, su_10, su_11 , su_12, su_13, 
                se_1, se_2, se_3, se_4, se_5, se_6, se_7, se_8, se_9, 
                sn_1, sn_2, sn_3, 
                sp_1, sp_2, sp_3, sp_4, sp_5, sp_6, sp_7, sp_8, sp_9, sp_10, sp_11, sp_12, sp_13, 
                sa_1, sa_2, sa_3, sa_4, sa_5, 
                be_1, be_2, be_3, be_4, be_5, be_6, be_7, be_8, be_9, be_10, be_11, be_12, be_13, 
                ka_1, ka_2, ka_3, ka_4, 
                sal_1, sal_2, sal_3]

        l_kk = ''
        for a in l_2:##Количество Проходимся по товарам и определяем не равныли их количество нулю
            for aa in l_1:#Имя. Проходимся по именам дабы количнство товара была потписана именем товара.
                if a != 0:#Проверяем не равна ли сумма 0
                    #Если сумма больше 0 то выводим имя и сумму
                    ty = f'{aa} = {a}, '
                    l_kk = l_kk + ty

                    l_1.pop(0)#Удаляем первый элемент спика чтобы когда цикл заново заработал он взял не снова первый элемент а уже следующий (второй)
                        
                    break#Останавливаем цикл
                        
                else :#Если сумма равна нулю то не выводим её
                    l_1.pop(0)#Удаляем первый элемент спика чтобы когда цикл заново заработал он взял не снова первый элемент а уже следующий (второй)
                    break

        now = datetime.datetime.now() 
        now2 = str(now)
        
        zp(l_kk, call.from_user.first_name, call.from_user.last_name, sis, now2)#Записываем информацию в базу данных
        ss2()#Выводим базу даннух

        #Отправляесм сообшение курьеру о том что и куда надо даставить
        soop = f'Заказ: {l_kk} \nИмя: {call.from_user.first_name}\n Фамилия: {call.from_user.last_name}\n Адрес: {sis}\n {now2}'
        ccron = 19563203855#id определённого человека (Курьера)
        bot.send_message(chat_id=ccron, text=soop)#Отпровляем сообщение конкретному человеку
        
        return l_kk
        
    def composition(compos1, compos2, compos3, compos4, compos5):

        bot.send_photo(call.message.chat.id, compos1)#Фото пиццы
        bot.send_message(call.message.chat.id, compos2)#Описание пиццы

        #Кнопки которые появляются после нажатия на преведущюю
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Добавить в корзину', callback_data=compos5))
        markup.add(telebot.types.InlineKeyboardButton(text='Вернутся', callback_data=compos4))

        bot.send_message(call.message.chat.id, text=compos3, reply_markup=markup)#Это саобщение к которому прикреплена кнопка
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)


 
    #Выбираем из ассортимента
#------------------------------------------------------------------
    if call.data == '1':
        PIZZA()
        
    elif call.data == '2':
        SUSHI()
        
    elif call.data == '3':
        SETS()

    elif call.data == '4':
        SNACKS()
        
    elif call.data == '5':
        SPECIAL_OFFERS()

    elif call.data == '6':
        SAUCES()
        
    elif call.data == '7':
        BEVERAGES()

    elif call.data == '8':
        KALZONE()

    elif call.data == '9':
        SALADS()

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
    #Описание товаров
    if call.data == '1.1':#То что происходит если нажать на первую пиццу
        composition('AgACAgIAAxkBAAIXBmE6h7OCk0Q0Wj5vMKMUkAICeaBCAAJWtDEbzGTYST02sy7FRw4mAQADAgADbQADIAQ', 
                    'Томаты и ананасы – это уже классика?\nСостав:  чесночный соус, грудка, ананасы, томаты, сыр', 
                    '270 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P1')

    elif call.data == '1.2':
        composition('AgACAgIAAxkBAAIXEWE6iOPOUalfZBvj6zAEyfDi3vbmAAJXtDEbzGTYSQbk5-ShGvUAAQEAAwIAA20AAyAE', 
                    'Грибная на соусе 1000 островов… Ммм… Состав: соус 1000 островов, грудка, опята, укроп, сыр ', 
                    '270 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P2')
    
    elif call.data == '1.3':
        composition('AgACAgIAAxkBAAIXEmE6ip-4KARJxp9Fl3J_zTpuUHgaAAJYtDEbzGTYSRFE9zzmJIRoAQADAgADbQADIAQ', 
                    'Семейная пицца – прямо, как дома!\nСостав: томатный соус, фарш, свежие шампиньоны, соленые огурчики, сыр', 
                    '270 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P3')
    
    elif call.data == '1.4':
        composition('AgACAgIAAxkBAAIXE2E6j_rZLINIzERnA985EZ6asSwNAAJatDEbzGTYSQhCK2NMtV4uAQADAgADcwADIAQ', 
                    'МОРСКАЯ пицца для любителей креветок\nСостав: сырный, соус, креветки, ананасы, сыр', 
                    '300 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P4')
    
    elif call.data == '1.5':
        composition('AgACAgIAAxkBAAIXFGE6kHIOqALWfW7Glc2XAAHDN384EgACW7QxG8xk2EmaNsuXREBLgAEAAwIAA3MAAyAE', 
                    'Пицца NINJA ДЖУНИОР лучший вариант для детей\nСостав: сырный соус ананасы сыр грудка', 
                    '270 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P5')
    
    elif call.data == '1.6':
        composition('AgACAgIAAxkBAAIXRWE7LpWY0RK-2Lwi8VWQ7HgDBK3BAALftDEbzGTYSawauk9XvMwVAQADAgADbQADIAQ', 
                    'Закон о рекламе запрещает нам использование сравнений!\nОднако мы не прочь сказать, что в ней нереальная доза твоего любимого сыра!\nА она - неожиданное воплощение всем знакомой классики...\nСостав: соус барбекю, пепперони, увеличенная порция сыра Моцарелла', 
                    '365 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P6')

    elif call.data == '1.7':
        composition('AgACAgIAAxkBAAIXSWE7V45i3JRrmWmy28x2Hrg2OGlXAAJCtzEbzGTgScolxMVandJ0AQADAgADbQADIAQ', 
                    'Ты жадно вкушаешь кусок этой пиццы!\nЗакрываешь глаза от удовольствия...\nИ произносишь одно единственное слово: "Сабай!"\nИ, вправду, с ней жизнь действительно хороша!\nСостав: соус томатный, соус кисло-сладкий, сыр, шампиньон, креветки, кунжут', 
                    '445 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P7')
   
    elif call.data == '1.8':
        composition('AgACAgIAAxkBAAIXT2E7WJw3V591qVuPFKMqGhd4lw4lAAJDtzEbzGTgSTTSPI5eGDz8AQADAgADbQADIAQ', 
                    'Чизо\nСостав: сырный соус, колбаски охотничьи, сыр, орегано', 
                    '325 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P8')

    elif call.data == '1.9':
        composition('AgACAgIAAxkBAAIXUGE7WdhdfXABSWNwiN0i4DdKFD4_AAJHtzEbzGTgSX_w5PkqpEAXAQADAgADbQADIAQ', 
                    'Да, это - любимая пицца Владислава Изместьева!\nИ иные слова тут лишние!\nСостав:Cоус Цезарь, ветчина, грудка копченая, шампиньоны свежие, сыр Моцарелла.', 
                    '365 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P9')

    elif call.data == '110':
        composition('AgACAgIAAxkBAAIXUWE7W1dynpDv01PKW7ULcF5hbZNtAAJJtzEbzGTgSXO0SKOVlvc6AQADAgADbQADIAQ', 
                    'Овощи Гриль\nСостав: соус томатный, куриная грудка, сыр, шампиньоны, перец, томаты Черри , сыр творожный, лук, соус песто', 
                    '385 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P10')

    elif call.data == '1.11':
        composition('AgACAgIAAxkBAAIXUmE7XCx5kBM8TFFijKbu011Q7bZPAAJLtzEbzGTgSYOc7baBatxzAQADAgADbQADIAQ', 
                    'Пицца Крейзи Пепперони\nСостав: кисло-сладкий соус, соус томатный, куриная грудка, сыр, пепперони', 
                    '385 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P11')

    elif call.data == '1.12':
        composition('AgACAgIAAxkBAAIXU2E7XVh6nkn0PdzqmIHXfw23qBMCAAJPtzEbzGTgSWLb6RnwKy4XAQADAgADbQADIAQ', 
                    'Пицца Сырная\nСостав: соус томатный, сыр, сыр творожный, орегано', 
                    '325 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P12')

    elif call.data == '1.13':
        composition('AgACAgIAAxkBAAIXVGE7XgZ35Vk-Ak4OlEhtI1qQGn6vAAJRtzEbzGTgSZYAAZgHbpzbdQEAAwIAA20AAyAE', 
                    'С ней непременно хочется поддаться соблазну!\nЗаказать себе любимому ее не в единственном экземпляре!\nИ растянуть аперитив на весь день!\nСостав: томатный соус, пепперони, сыр, перец, соус "Бургер", свежие томаты, красный лук', 
                    '345 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P13')

    elif call.data == '1.14':
        composition('AgACAgIAAxkBAAIXVWE7YeC_I9TCtvjITM60zffJO2cgAAJgtzEbzGTgSbcy9WTLH5KcAQADAgADbQADIAQ', 
                    'Приготовьтесь!\nСейчас будет мясо!\nДа стооолько, что вы ненароком подумайте...\nЧто мы грабанули один не безызвестный мясокомбинат.\nСостав:Соус барбекю, охотничьи колбаски, ветчина, сочная курица, бекон, соленые огурчики, сыр моцарелла, лук.', 
                    "385 ₽", 
                    'RETURN_BACK_P', 
                    'ADDITION_P14')
    
    elif call.data == '1.15':
        composition('AgACAgIAAxkBAAIXV2E7Yr-Y7C0F0WDwo_V5DX0nS6aEAAJitzEbzGTgSROrBSFQGpkbAQADAgADbQADIAQ', 
                    'Сегодня ты не открываешь пачку чипсов!\nТы открываешь коробку и задаешь нам только один вопрос:\nТак можно было?\nМы же отвечаем тебе неповторимым вкусом и нереальным сочетанием ингредиентов!\nСостав: куриная грудка, картофель фри, соус Цезарь, сыр Моцарелла, свежие томаты, огурцы, красный лук', 
                    '355 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P15')

    elif call.data == '1.16':
        composition('AgACAgIAAxkBAAIXcWE7xWQ7VAABDAWRonDn5iboBrXZogACbbgxG8xk4EnZnQNKuHFIFQEAAwIAA20AAyAE', 
                    'Имеем ли мы право сказать, что с горячестью этой цыпы ничто (и никто) не сравнится?\nДумаем, нет!\nНо ты можешь об этом подумать!\nСостав: пепперони, томатный соус, остро-сладкий соус, куриная грудка', 
                    '345 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P16')

    elif call.data == '1.17':
        composition('AgACAgIAAxkBAAIXcmE7xeNijBsPbkgkKnERoxRIh9jrAAJuuDEbzGTgSa3Ow2i7gssbAQADAgADbQADIAQ', 
                    'Пицца Ниндзя Опята\nСостав: соус чесночный, охотничьи колбаски, ветчина, сыр, бекон, опята, свежие томаты', 
                    '385 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P17')

    elif call.data == '1.18':
        composition('AgACAgIAAxkBAAIXc2E7xnKtZJRhwaN9fWEnP2YgurYCAAJyuDEbzGTgSbb8iSsdg9HYAQADAgADbQADIAQ', 
                    'После поедания этой пиццы,\nвам внезапно может показаться...\nЧто вы знатно покуражились на шашлыках.\nБросайте барбекюшницы, красотка уже в печи!\nСостав:Томатный соус, цыплёнок, бекон, красный лук, соус барбекю, сыр моцарелла.', 
                    '365 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P18')

    elif call.data == '1.19':
        composition('AgACAgIAAxkBAAIXdGE7xsSIU6T6ifEmh0QyjJEDBrl6AAJzuDEbzGTgSWgkWK5VcX4CAQADAgADbQADIAQ', 
                    'Пицца Сырный Цыпленок\nСостав: сырный соус, куриная грудка, сыр, томаты', 
                    '355 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P19')

    elif call.data == '120':
        composition('AgACAgIAAxkBAAIXdWE7x9JNpei_EEwFJjBn1Q9EjROqAAJ1uDEbzGTgSaVL2H2_zBuLAQADAgADbQADIAQ', 
                    'Именно за ней охотятся главные вегетарианцы города.\nИ правильно делают.\nТакого обилия овощного-грибного бомбического нет нигде.\nСостав:Томатный соус, шампиньоны, сладкий перец, красный лук, маслины, томаты, сыр фета, сыр Моцарелла.', 
                    '345 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P20')

    elif call.data == '1.21':
        composition('AgACAgIAAxkBAAIXdmE7yOAhbpHk8GpOTWQ0zuqNc23rAAJ2uDEbzGTgSYhR3b2CxYYmAQADAgADbQADIAQ', 
                    'Пицца Шредер\nСостав: соус томатный, куриная грудка, сыр, шампиньоны, перец, томаты , халапеньо, лук', 
                    '365 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P21')

    elif call.data == '1.22':
        composition('AgACAgIAAxkBAAIXd2E7ySLteaLapXIbfOijT6Hn1KkUAAJ3uDEbzGTgScvWnXsIKE55AQADAgADbQADIAQ', 
                    'Да, это она!\nПокорительница вегетарианских сердец.\nСохранительница прокаченных тел.\nПоздоровайтесь!\nСостав:Томатный соус, томаты, орегано, увеличенная порция сыра моцарелла.', 
                    '335 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P22')

    elif call.data == '1.23':
        composition('AgACAgIAAxkBAAIXeGE7ybt7B3lVErvXCF393_aSfLlaAAJ4uDEbzGTgSZt03SyPmuZcAQADAgADbQADIAQ', 
                    'Пицца Ранч\nСостав: соус чесночный, ветчина, куриная грудка, сыр, свежие томаты', 
                    '365 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P23')

    elif call.data == '1.24':
        composition('AgACAgIAAxkBAAIXeWE7yqWRhnU7Nj-LPN6swmcelMJEAAJ6uDEbzGTgSZxfqnfLPP09AQADAgADbQADIAQ', 
                    'Не знаем...\nИтальянец али нет этот засланный гонец.\nНо пожиратели сходят с ума от его заморского акцента.\nСостав:Томатный соус, цыпленок, колбаски пепперони, красный лук, бекон, сыр моцарелла.', 
                    '365 ₽', 
                    'RETURN_BACK_P',
                    'ADDITION_P24')

    elif call.data == '1.25':
        composition('AgACAgIAAxkBAAIXemE7ziSyVzx2MmoehRv1V6PBBcwrAAJ9uDEbzGTgSaLzlerdFyQMAQADAgADbQADIAQ', 
                    'Кавабанга\nСостав: соус томатный, ветчина, сыр, пепперони, шампиньоны, сладкий перец, маслины, лук', 
                    '385 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_25')

    elif call.data == '1.26':
        composition('AgACAgIAAxkBAAIXe2E7zpykdvvV01NP4IzOqyyNy7AyAAJ-uDEbzGTgSeI4oWq7GuzzAQADAgADbQADIAQ', 
                    'Тот самый бургер, который делится на биг-компани.\nИли не делится...\nЭто уж вам решать!\nСостав:Сырный соус, грудка копченая, охотничьи колбаски, бекон, солёные огурчики, красный лук, томаты, сыр моцарелла.', 
                    '385 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P26')

    elif call.data == '1.27':
        composition('AgACAgIAAxkBAAIXfGE7zxRqzuNFnekl1Pu6oxoDKsxuAAKAuDEbzGTgSdMIZzsFz3FdAQADAgADbQADIAQ', 
                    'Пицца Ниндзяго (30 см)\nСостав: соус Барбекю, куриная грудка, сыр, шампиньон, сладкий перец, свежие томаты, маслины, сыр творожный, лук', 
                    '375 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P27')

    elif call.data == '1.28':
        composition('AgACAgIAAxkBAAIXfWE7z4C7UUaqhq9ueCy6SKIO5yYKAAKCuDEbzGTgSWfMY_05T_N4AQADAgADbQADIAQ', 
                    'Четыре сыра\nСостав: томатный соус, сыр Чеддер, пармезан, сыр Моцарелла, сыр Дорблю', 
                    '385 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P28')

    elif call.data == '1.29':
        composition('AgACAgIAAxkBAAIXfmE7z9sHrn1HY7Ve2wlBshTTMELJAAKDuDEbzGTgSXMso8uUVzUJAQADAgADbQADIAQ', 
                    'Пицца Ниндзя Италия\nСостав: соус томатный, пепперони, куриная грудка, сыр, шампиньон, маслины, орегано', 
                    '365 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P29')

    elif call.data == '130':
        composition('AgACAgIAAxkBAAIXf2E70EE4bjLzb9iUWMEJjJHlA28mAAKEuDEbzGTgSXp_OHMGT2omAQADAgADbQADIAQ', 
                    'Есть подозрение, что скоро Сэнсэй появится на обложке Mens Health.\nИбо ничего более брутальнее в нашем меню нет!\nСостав: соус горчичный, колбаски пепперони, ветчина, грудка копченая, сыр Моцарелла, бекон, охотничьи колбаски.', 
                    '395 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P30')

    elif call.data == '1.31':
        composition('AgACAgIAAxkBAAIXgGE70PbBNkyO1yA3cUgqF4hTbGn4AAKFuDEbzGTgScgyJif15ihxAQADAgADbQADIAQ', 
                    'Будьте осторожны!\nПосле этой чертовки хочется больше необычных сочетаний в жизни!\nА ее, конечно, хочется ещё больше!\nСостав:Томатный соус, ветчина, цыпленок, бекон, ананас, сыр моцарелла', 
                    '375 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P31')

    elif call.data == '1.32':
        composition('AgACAgIAAxkBAAIXgWE70VWvZLte_wABiWGlZ-Ru1HbKmgAChrgxG8xk4EnUWYVQs9Oa6QEAAwIAA20AAyAE', 
                    'Эта красотка может смело поконкурировать с Ольгой Бузовой.\nПо популярности, конечно.\nИ мы даже знаем, кто тут победитель.\nСостав:Соус барбекю, охотничьи колбаски, колбаски пепперони, увеличенная порция сыра моцарелла.', 
                    '365 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P32')

    elif call.data == '1.33':
        composition('AgACAgIAAxkBAAIXgmE70bnI1m7idn-RLRyMl0N9p_LvAAKLuDEbzGTgSbMXzRO4UFZSAQADAgADbQADIAQ', 
                    'Когда-то Мэри Джейн покорила сердце Питера Паркера!\nТы, конечно, не человек-паук...\nНо твое сердце будет разбито ею не с меньшим успехом!\nСостав: молоко сгущеное, ореховый микс, сыр Моцарелла, бананы, яблоки, ананасы.', 
                    '365 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P33')

    elif call.data == '1.34':
        composition('AgACAgIAAxkBAAIXg2E70h7_d3U-jomnp3oeYwS8lwKkAAKMuDEbzGTgSeMWVChzX5EfAQADAgADbQADIAQ', 
                    'Акуна Матата\nСостав: сырный соус, сыр, томаты, шампиньоны, грудка, жареный лук', 
                    '345 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P34')

    elif call.data == '1.35':
        composition('AgACAgIAAxkBAAIXhGE70oeunx91gktxkMie8IN1S4LyAAKNuDEbzGTgSdDjZhKB8KtXAQADAgADbQADIAQ', 
                    'Предупреждаем: у этой пиццы есть один побочный эффект!\nВо время ее поедания бедра сами делают "восьмерку"...\nА после – ты не можешь себя сдерживать и идешь учиться игре на укулеле!\nСостав: ананасы, сыр Моцарелла, соус "Терияки", томатный соус, куриная грудка', 
                    '345 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P35')

    elif call.data == '1.36':
        composition('AgACAgIAAxkBAAIXhWE70xxZJ6wq9jR8O5it94il7uL2AAKOuDEbzGTgSbgDR7LhM2L9AQADAgADbQADIAQ', 
                    'Пепперони Фреш\nСостав: соус Барбекю, сыр, пепперони, свежие томаты', 
                    '325 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P36')

    elif call.data == '1.37':
        composition('AgACAgIAAxkBAAIXhmE702xEvnMX8MlBXQ6QTJqeRTgrAAKPuDEbzGTgSUDEfSW5mgeTAQADAgADbQADIAQ', 
                    'Будь осторожен!\nПосле - тебя не спасет ни стакан молока, ни жвачка...\nИ, да, ты можешь смело забыть о мысли, что пицца не вызывает привыкания!\nСостав: сладкий перец Чили, шампиньоны, пепперони, халапеньо, болгарский перец', 
                    '355 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P37')

    elif call.data == '1.38':
        composition('AgACAgIAAxkBAAIXh2E70__Qjq5-XKOEk02o4_iYez2eAAKSuDEbzGTgSUV8Hh7UxElFAQADAgADbQADIAQ', 
                    'Сладкий Цыпа\nСостав: соус томатный, куриная грудка, сыр, кисло-сладкий соус', 
                    '335 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P38')

    elif call.data == '1.39':
        composition('AgACAgIAAxkBAAIXiGE71IMwFkFWB7wxqlAjKtR3ix1OAAKTuDEbzGTgSeOgQKtc1VMgAQADAgADbQADIAQ', 
                    'Пицца Ниндзя Гавайи\nСостав: соус 1000 островов, ветчина, куриная грудка, сыр, ананасы', 
                    '365 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P39')

    elif call.data == '140':
        composition('AgACAgIAAxkBAAIXiWE71N9jvpuRkBKHvh1yLsjyvBifAAKUuDEbzGTgSW-huaOaGAexAQADAgADbQADIAQ', 
                    'Секрет идеальной смородины, что оказалась в этой пицце, пытаются узнать все садоводы Можги!\nИ, да, её количество на окружность в 30 см поражает даже бабушек на рынке!\nСостав: черная смородина, яблоко, сгущенное молоко, сыр Моцарелла, корица', 
                    '365 ₽', 
                    'RETURN_BACK_P', 
                    'ADDITION_P40')









    if call.data == '2.1':
        composition('AgACAgIAAxkBAAIXtWE71pmQynYzs2lWa2roDymQPN86AAKVuDEbzGTgSfvXyfBScK9bAQADAgADbQADIAQ', 
                    'Подается с соевым соусом, имбирем и пастой васаби.\nПорция 8 шт - 230/20/20 гр.\nГолубой Рис, Нори, Сыр Филадельфия, Свежий Огурец, Филе Лосося, Соус Унаги', 
                    '250 ₽', 
                    'RETURN_BACK_SU',
                    'ADDITION_SU1')

    elif call.data == '2.2':
        composition('AgACAgIAAxkBAAIXvmE72U8BOInNNsMYhwABbqRN1Bur1gACl7gxG8xk4En9B1Ie8qWGogEAAwIAA20AAyAE', 
                    'Подается с соевым соусом, имбирем и пастой васаби.\nПорция 8 шт - 230/20/20/20 гр.\nГолубой Рис, Нори, Сыр Филадельфия, Свежий Огурец, Соус Шрирача (острый), Угорь\nСоус Унаги, омлет', 
                    '260 ₽', 
                    'RETURN_BACK_SU',
                    'ADDITION_SU2')
    
    elif call.data == '2.3':
        composition('AgACAgIAAxkBAAIXv2E72dxU9yao_6A80QTsfO9BCmSHAAKZuDEbzGTgSVyfAAGJ_OAlzQEAAwIAA20AAyAE', 
                    'Подается с соевым соусом, имбирем и пастой васаби.\nПорция 8 шт - 230/20/20/20 гр.\nГолубой Рис, Нори, Сыр Филадельфия, Филе Тунца, Свежий Огурец, Соус Унаги,Кунжут', 
                    '250 ₽', 
                    'RETURN_BACK_SU',
                    'ADDITION_SU3')
    
    elif call.data == '2.4':
        composition('AgACAgIAAxkBAAIXwGE72o_GiyJuRxxuN8pbnfCQoKF4AAKbuDEbzGTgSSX7o7IKIzYuAQADAgADbQADIAQ', 
                    'Подается с соевым соусом, имбирем и пастой васаби \nПорция 8 шт - 230/20/20/20 гр.\nГолубой Рис, Нори, Сыр Филадельфия, Авокадо, Огурец Свежий, Филе Лосося', 
                    '250 ₽', 
                    'RETURN_BACK_SU',
                    'ADDITION_SU4')
    
    elif call.data == '2.5':
        composition('AgACAgIAAxkBAAIXwWE72xkC7L4vZxgeFkBxBfzB51HvAAKcuDEbzGTgSd-5v5x3g7ENAQADAgADbQADIAQ', 
                    'Подается с соевым соусом, имбирем и пастой васаби.\nПорция 8 шт - 230/20/20/20 гр.\nГолубой Рис, Нори, Сыр Филадельфия, Опалённый Лосось, Креветка, Тростниковый Сахар (тропический)', 
                    '260 ₽', 
                    'RETURN_BACK_SU',
                    'ADDITION_SU5')
    
    elif call.data == '2.6':
        composition('AgACAgIAAxkBAAIXwmE73MZ7e0Nl4ZkiEQoHg3uc0jvgAAKduDEbzGTgSTLF5i725g19AQADAgADbQADIAQ', 
                    'Подается с соевым соусом, имбирем и пастой васаби.\nПорция 8 шт - 250/20/20/20 гр.\nРис, сыр Филадельфия, нори, Свежий огурец, Сливочный Мусс с лососем', 
                    '250 ₽', 
                    'RETURN_BACK_SU',
                    'ADDITION_SU6')

    elif call.data == '2.7':
        composition('AgACAgIAAxkBAAIXw2E73TjLOFNxFrhO-DwnTPFz63yaAAKeuDEbzGTgSTVCDeYvq8IBAQADAgADbQADIAQ', 
                    'Подается с соевым соусом, имбирем и пастой васаби.\nПорция 8 шт - 250/20/20/20 гр.\nГолубой Рис, Нори, Куриная грудка, Сыр Филадельфия, Свежий Огурец, Мусс сливочный', 
                    '230 ₽', 
                    'RETURN_BACK_SU',
                    'ADDITION_SU7')
   
    elif call.data == '2.8':
        composition('AgACAgIAAxkBAAIXxGE73cMPdbkKcTDdAmIVlgeDBa1BAAKfuDEbzGTgSTkxZvihfTmeAQADAgADbQADIAQ', 
                    'Подается с соевым соусом, имбирем и пастой васаби.\nПорция 8 шт - 230/20/20 гр.\nГолубой Рис, Нори, Сыр Филадельфия, Омлет, Свежий Огурец, Курица кимчи, Соус Ким Чи, Соус терияки, Кунжут', 
                    '220 ₽', 
                    'RETURN_BACK_SU',
                    'ADDITION_SU8')

    elif call.data == '2.9':
        composition('AgACAgIAAxkBAAIXxWE73mFmtuFxAVI7qd7iFNrnQbRaAAKhuDEbzGTgSaOND0BN2j4PAQADAgADbQADIAQ', 
                    'Подается с соевым соусом, имбирем и пастой васаби.\nПорция 8 шт - 250/20/20/20 гр.\nСостав: голубой рис, нори, сыр Филадельфия, авокадо, креветка, кляр, соус Унаги', 
                    '250 ₽', 
                    'RETURN_BACK_SU',
                    'ADDITION_SU9')

    elif call.data == '210':
        composition('AgACAgIAAxkBAAIXxmE73t5ZPzEs3urIq6uqxMTgky9GAAKiuDEbzGTgSWuC839HL3KNAQADAgADbQADIAQ', 
                    'Подается с соевым соусом, имбирем и пастой васаби.\nПорция 8 шт - 250/20/20/20 гр.\nГолубой Рис, Нори, Свежий Огурец, Омлет, Соус Терияки, Кунжут', 
                    '220 ₽', 
                    'RETURN_BACK_SU',
                    'ADDITION_SU10')

    elif call.data == '2.11':
        composition('AgACAgIAAxkBAAIXx2E730rDWZNTvxUYA2hZPxSaGS4oAAKjuDEbzGTgSdOiMlVv7QJCAQADAgADbQADIAQ', 
                    'Подается с соевым соусом, имбирем и пастой васаби.\nПорция 8 шт - 250/20/20/20 гр.\nГолубой Рис, Нори, Тунец, Омлет, Сыр Филадельфия, Свежий Огурец', 
                    '240 ₽', 
                    'RETURN_BACK_SU',
                    'ADDITION_SU11')

    elif call.data == '2.12':
        composition('AgACAgIAAxkBAAIXyGE7362shHf39t4RF1YfduBUSlF5AAKkuDEbzGTgSTzebjLLs_-zAQADAgADbQADIAQ', 
                    'Подается с соевым соусом, имбирем и пастой васаби.\nПорция 8 шт - 250/20/20/20 гр.\nГолубой Рис, Нори, Сыр Филадельфия, Омлет, Свежий Огурец, Соус Унаги, Кунжут', 
                    '250 ₽', 
                    'RETURN_BACK_SU',
                    'ADDITION_SU12')

    elif call.data == '2.13':
        composition('AgACAgIAAxkBAAIXyWE74FCxfQrZ_DQJDz2QP_N64F5cAAKluDEbzGTgSTeMsRxjmmaAAQADAgADbQADIAQ', 
                    'Подается с соевым соусом, имбирем и пастой васаби.\nПорция 8 шт - 250/20/20/20 гр.\nГолубой Рис, Нори, Сыр Филадельфия, Свежий Огурец, Филе Лосося, Соус Унаги', 
                    '240 ₽', 
                    'RETURN_BACK_SU',
                    'ADDITION_SU13')








    if call.data == '3.1':
        composition('AgACAgIAAxkBAAIX_WE74TJYqoYWAdxmirqTDZ-2eYpQAAKmuDEbzGTgSWiOnvrTX91cAQADAgADbQADIAQ', 
                    'Состав: классика с огурцом, темпура с бататом, ролл запеченый шиитаке, ролл фреш хан.\nВес - 32шт\nК каждой порции мы кладём имбирь, васаби и соевый соус)', 
                    '390 ₽', 
                    'RETURN_BACK_SE',
                    'ADDITION_SE1')

    elif call.data == '3.2':
        composition('AgACAgIAAxkBAAIYCGE8Vm_CUv3QEb6yc86uS9qKHYZ9AALwtjEb6vXgSaMCMgOKX4EHAQADAgADbQADIAQ', 
                    'Состав: ролл филадельфия с угрем, ролл классика с огурцом, ролл филадельфия с тунцом, ролл темпура с тунцом, ролл классика с омлетом, ролл темпура с курицей.\nВес - 48 шт\nК каждой порции мы кладем имбирь, васаби и соевый соус)', 
                    '845 ₽', 
                    'RETURN_BACK_SE',
                    'ADDITION_SE2')
    
    elif call.data == '3.3':
        composition('AgACAgIAAxkBAAIYCWE8VuA12R-fo6nSJJY2m3dnLP2DAALxtjEb6vXgSc-F2EjD4WfYAQADAgADbQADIAQ', 
                    'Состав: темпура с курицей, темпура с мидиями, темпура с бататом , темпура с креветкой!\nВес 1000гр - 32шт 🤤\nК каждой порции мы кладем имбирь, васаби и соевый соус)', 
                    '690 ₽', 
                    'RETURN_BACK_SE',
                    'ADDITION_SE3')
    
    elif call.data == '3.4':
        composition('AgACAgIAAxkBAAIYCmE8WQ80h9rHMPUdMJBdqu0BOYcvAALztjEb6vXgSbU2epe4gGjcAQADAgADbQADIAQ', 
                    'Состав: ролл филадельфия с лососем, темпура с креветкой, ролл чикен терияки.\nВес - 24 шт\nК каждой порции мы кладем имбирь, васаби и соевый соус)', 
                    '545 ₽', 
                    'RETURN_BACK_SE',
                    'ADDITION_SE4')
    
    elif call.data == '3.5':
        composition('AgACAgIAAxkBAAIYEGE8WcyULpZYGLLJCILMo-vGSKoSAAL0tjEb6vXgSQR9AQHevcuYAQADAgADbQADIAQ', 
                    'Состав: ролл темпура с курицей, ролл филадельфия с тунцом, ролл фреш хан!\nВес - 24 шт\nК каждой порции мы кладем имбирь, васаби и соевый соус)', 
                    '490 ₽', 
                    'RETURN_BACK_SE',
                    'ADDITION_SE5')
    
    elif call.data == '3.6':
        composition('AgACAgIAAxkBAAIYEWE8WyZ-nupk-doiXcTNL2HoeFLlAAL2tjEb6vXgSVIwBy-dIpbQAQADAgADbQADIAQ', 
                    'Состав: ролл фреш хан, ролл темпура батат, ролл темпура с мидиями, ролл филадельфия с угрем, ролл сёгун, ролл запечённый с курицей, ролл слэш, ролл карай.\nВес - 1600гр - 64 шт\nК каждому роллу мы кладем имбирь, васаби и соевый соус)', 
                    '990 ₽', 
                    'RETURN_BACK_SE',
                    'ADDITION_SE6')

    elif call.data == '3.7':
        composition('AgACAgIAAxkBAAIYEmE8W8cz7gi2p225QegB5q1Umu67AAL3tjEb6vXgSSHMqL7_DODsAQADAgADbQADIAQ', 
                    'Состав: ролл филадельфия с угрем, ролл филадельфия с лососем, ролл мураками, ролл слэш!\nВес - 32 шт.\nК каждой порции мы кладем имбирь, васаби и соевый соус)', 
                    '745 ₽', 
                    'RETURN_BACK_SE',
                    'ADDITION_SE7')
   
    elif call.data == '3.8':
        composition('AgACAgIAAxkBAAIYE2E8XG8N96wAAUuJjEfYr6ich_eUKQAC-LYxG-r14En5Og9ldHN10AEAAwIAA20AAyAE', 
                    'Состав: ролл карай, запечный с шиитаке, ролл слэш, ролл шинигами\nВес - 34 шт\nК каждой порции мы кладем имбирь, васаби и соевый соус :-)', 
                    '590 ₽', 
                    'RETURN_BACK_SE',
                    'ADDITION_SE8')

    elif call.data == '3.9':
        composition('AgACAgIAAxkBAAIYFGE8XNd2zZgDXmSsZF6ExxGnNLeVAAL5tjEb6vXgSR-lcmcUu5vrAQADAgADbQADIAQ', 
                    'Состав: маки с креветкой , маки с омлетом , маки с тунцом , маки с авокадо , маки с курицей, маки огурцом.\nВес - 48 штК каждой порции мы кладем имбирь, васаби и соевый соус)', 
                    '490 ₽', 
                    'RETURN_BACK_SE',
                    'ADDITION_SE9')







    if call.data == '4.1':
        composition('AgACAgIAAxkBAAIYLmE8Xptkkevn35Jnf2mAbSJGB6XMAAL8tjEb6vXgSZ1pi0TJSuPuAQADAgADbQADIAQ', 
                    'Картофель фри\nВес: 200 гр', 
                    '100 ₽', 
                    'RETURN_BACK_SN',
                    'ADDITION_SN1')

    elif call.data == '4.2':
        composition('AgACAgIAAxkBAAIYL2E8YD4G8OqBRe4AATtPJSDlgH6csgAC_rYxG-r14EmigZcQ1XtVwAEAAwIAA20AAyAE', 
                    'Картофельные дольки\nВес: 200 гр', 
                    '100 ₽', 
                    'RETURN_BACK_SN',
                    'ADDITION_SN2')
    
    elif call.data == '4.3':
        composition('AgACAgIAAxkBAAIYMGE8YJYhZTv_ITmST4kIeOk7it2BAAL_tjEb6vXgSTPcAAHQvHPNFAEAAwIAA20AAyAE', 
                    'Куриное филе в фирменной панировке\nВес: 200 гр', 
                    '100 ₽', 
                    'RETURN_BACK_SN',
                    'ADDITION_SN3')







    if call.data == '5.1':
        composition('AgACAgIAAxkBAAIYRWE8YyzuVchibVSFmaNmSWA_81bnAAICtzEb6vXgSdA7-KS9Rda9AQADAgADbQADIAQ', 
                    'Предложение не суммируется с другими акциями\nНиндзя-бонусы при заказе комбо не начисляются\nВ акции участвуют все пиццы из Ниндзя-меню', 
                    '3190 ₽', 
                    'RETURN_BACK_SP',
                    'ADDITION_SP1')

    elif call.data == '5.2':
        composition('AgACAgIAAxkBAAIYRmE8fwq2QjxC8vFGkXxuwdt7-GFFAAJFtzEb6vXgSdjqCLNqknfKAQADAgADbQADIAQ', 
                    'Предложение не суммируется с другими акциями\nНиндзя-бонусы при заказе комбо не начисляются\nВ акции участвуют все пиццы из Ниндзя-меню', 
                    '990 ₽', 
                    'RETURN_BACK_SP',
                    'ADDITION_SP2')
    
    elif call.data == '5.3':
        composition('AgACAgIAAxkBAAIYR2E8gPNeARNZxMTyEdQAAX-mGXWBWQACTbcxG-r14EnH7Ch1gU2AIAEAAwIAA20AAyAE', 
                    'Предложение не суммируется с другими акциями\nНиндзя-бонусы при заказе комбо не начисляются\nВ акции участвуют все пиццы из Ниндзя-меню', 
                    '1145 ₽', 
                    'RETURN_BACK_SP',
                    'ADDITION_SP3')
    
    elif call.data == '5.4':
        composition('AgACAgIAAxkBAAIYSGE8gXerOHzhbcSOSrCYkjTAIBsKAAJOtzEb6vXgScA5HPCKg8JjAQADAgADbQADIAQ', 
                    'Предложение не суммируется с другими акциями\nНиндзя-бонусы при заказе комбо не начисляются\nВ акции участвуют все пиццы из Ниндзя-меню', 
                    '690 ₽', 
                    'RETURN_BACK_SP',
                    'ADDITION_SP4')
    
    elif call.data == '5.5':
        composition('AgACAgIAAxkBAAIYSWE8jWz_W-0kA5w2FMaVuJ7lEoyyAAJwtzEb6vXgSdDVH2239WFnAQADAgADbQADIAQ', 
                    'Семь пицц по супер-цене\nПредложение не суммируется с другими акциями\nНиндзя-бонусы при заказе комбо не начисляются\nВ акции участвуют все пиццы из Ниндзя-меню', 
                    '2290 ₽', 
                    'RETURN_BACK_SP',
                    'ADDITION_SP5')
    
    elif call.data == '5.6':
        composition('AgACAgIAAxkBAAIYSmE8jeORWcVKctvtxD7yWtRaaBWEAAJztzEb6vXgSfuJOYNDTNUhAQADAgADbQADIAQ', 
                    'Одна большая пицца + картофель фри + напиток (0,5 литров)\nПредложение не суммируется с другими акциями\nНиндзя-бонусы при заказе комбо не начисляются\nВ акции участвуют все пиццы из Ниндзя-меню', 
                    '545 ₽', 
                    'RETURN_BACK_SP',
                    'ADDITION_SP6')

    elif call.data == '5.7':
        composition('AgACAgIAAxkBAAIYS2E8jo3AYoXnjTISfUYyIIy0kKa4AALGtzEb6vXoSa5sVUO5nLDTAQADAgADbQADIAQ', 
                    'Картофель фри + картофельные дольки + напиток\nПредложение не суммируется с другими акциями\nНиндзя-бонусы при заказе комбо не начисляются', 
                    '270 ₽', 
                    'RETURN_BACK_SP',
                    'ADDITION_SP7')
   
    elif call.data == '5.8':
        composition('AgACAgIAAxkBAAIYTGE8jvd6bKj_G2yEBOViihwpGnQhAALItzEb6vXoSbzALPldbx1CAQADAgADbQADIAQ', 
                    'Две пиццы (25 см) + напиток (1 литр)\nПредложение не суммируется с другими акциями\nНиндзя-бонусы при заказе комбо не начисляются\nВ акции участвуют все пиццы из Ниндзя-меню и все напитки в объеме 1 литр', 
                    '545 ₽', 
                    'RETURN_BACK_SP',
                    'ADDITION_SP8')

    elif call.data == '5.9':
        composition('AgACAgIAAxkBAAIYh2E9m-0bKOA9CZHgYs_IHqWNZwzaAALLtzEb6vXoSQNXNllB0hmEAQADAgADbQADIAQ', 
                    'Нет, если ты просишь...\nТо мы просто не можем отказать!\nИ продолжаем сводить тебя с ума...\nВыгодой. Вкусом. Скоростью доставки☄\nДа, две большие пиццы. Только сейчас!\nВсего за 790 рублей🔥', 
                    '790 ₽', 
                    'RETURN_BACK_SP',
                    'ADDITION_SP9')

    elif call.data == '510':
        composition('AgACAgIAAxkBAAIYiGE9nJ8zhVrLQC51nzb6sdradp-8AAIltjEb6vXwSewa_hBJZ1ycAQADAgADbQADIAQ', 
                    '"Мы заказали две в одной!\nНе трогай мою половину!"\nНу, чем не аргумент?\nСтоимость рассчитывается исходя из выбранных пицц', 
                    '1 ₽', 
                    'RETURN_BACK_SP',
                    'ADDITION_SP10')

    elif call.data == '5.11':
        composition('AgACAgIAAxkBAAIYiWE9nSfxKT81J957XV7k4Qs40N-cAAIntjEb6vXwSdQMgi4bLAlUAQADAgADbQADIAQ', 
                    'Только не ругайся!\nМы соединили в одном сете три твоих любимых пиццы...\nИ не оставили никаких шансов заказать одну из них в единственном экземпляре!\nСкорее собирай друзей!\nПредупреждай, что самая большая будет твоей!', 
                    '840 ₽', 
                    'RETURN_BACK_SP',
                    'ADDITION_SP11')

    elif call.data == '5.12':
        composition('AgACAgIAAxkBAAIYimE9nd_oDySKslEZ8kCyWH6L3X78AAIptjEb6vXwSZdW4mokpU5jAQADAgADbQADIAQ', 
                    'Неважно, где лучшие тусовки!\nВажно лишь то, что с пиццей в зубах!\nДавайте вместе двигать бедрами!\nМы приготовили для вас крайне заманчивое предложение!\nДве любимые пиццы + 2 картошки фри = 820 рублей + кола в ПОДАРОК!', 
                    '820 ₽', 
                    'RETURN_BACK_SP',
                    'ADDITION_SP12')

    elif call.data == '5.13':
        composition('AgACAgIAAxkBAAIYi2E9nk1QMiMK6FEWCWwYC2uqReooAAIqtjEb6vXwSf1qqKt8c4svAQADAgADbQADIAQ', 
                    'Сумасшедшее предложение для большой компании...\nИли одного голодного тебя!\nШесть пицц по чертовски выгодной цене!\nЦыплёнок Барбекю + Сырный Цыплёнок + Микеланджело + Донателло + Рафаэль + Ранч = 1560 рублей (вместо: 1860 рублей).', 
                    '1560 ₽', 
                    'RETURN_BACK_SP',
                    'ADDITION_SP13')







    if call.data == '6.1':
        composition('AgACAgIAAxkBAAIYoGE9oKDBJLQrBwjhdDUkDS2bMZ6eAAIrtjEb6vXwSWJhUE894OHRAQADAgADbQADIAQ', 
                    'Соус чесночный', 
                    '15 ₽', 
                    'RETURN_BACK_SA',
                    'ADDITION_SA1')

    elif call.data == '6.2':
        composition('AgACAgIAAxkBAAIYoWE9oPkvrhBAbB0DCFzLxXlaxztGAAIstjEb6vXwSWKhT-63_yGEAQADAgADbQADIAQ', 
                    'Томатный соус', 
                    '15 ₽', 
                    'RETURN_BACK_SA',
                    'ADDITION_SA2')
    
    elif call.data == '6.3':
        composition('AgACAgIAAxkBAAIYomE9oTqgOUIEeoFQcE9vEZSaW6QvAAIttjEb6vXwSZh7G7Bk2JAYAQADAgADbQADIAQ', 
                    'Соус сырный', 
                    '15 ₽', 
                    'RETURN_BACK_SA',
                    'ADDITION_SA3')
    
    elif call.data == '6.4':
        composition('AgACAgIAAxkBAAIYo2E9oYQFAT8LiJaqy3NzLI9mfbuGAAIutjEb6vXwSXUF5oj8cmtcAQADAgADbQADIAQ', 
                    'Кисло-сладкий соус', 
                    '15 ₽', 
                    'RETURN_BACK_SA',
                    'ADDITION_SA4')
    
    elif call.data == '6.5':
        composition('AgACAgIAAxkBAAIYpGE9ocHhGKWow21Lo_kqJvHNMrGDAAIwtjEb6vXwSSVPemvtdM72AQADAgADbQADIAQ', 
                    'Соус барбекю', 
                    '15 ₽', 
                    'RETURN_BACK_SA',
                    'ADDITION_SA5')






    if call.data == '7.1':
        composition('AgACAgIAAxkBAAIYyWE98E0x4UYHVhcMXFADMP-n8IERAAIWtzEb6vXwSXoOzmb_IbYPAQADAgADbQADIAQ', 
                    'Сок Rich Яблоко ',
                    '140 ₽', 
                    'RETURN_BACK_BE',
                    'ADDITION_BE1')

    elif call.data == '7.2':
        composition('AgACAgIAAxkBAAIYyGE96W4Z6hzZHCW9siJnP5DBBoPFAAIMtzEb6vXwSTuE1R5peza9AQADAgADbQADIAQ', 
                    'Сок Rich Персик', 
                    '140 ₽', 
                    'RETURN_BACK_BE',
                    'ADDITION_BE2')
    
    elif call.data == '7.3':
        composition('AgACAgIAAxkBAAIYymE98HW3HUjnCf9bPwsMQnjFVQljAAIZtzEb6vXwSc8PoG53WkdtAQADAgADbQADIAQ', 
                    'Сок Rich Мультифрукт', 
                    '140 ₽', 
                    'RETURN_BACK_BE',
                    'ADDITION_BE3')
    
    elif call.data == '7.4':
        composition('AgACAgIAAxkBAAIYy2E98KRJH46ybBPeyt6CWg-ohTuZAAIatzEb6vXwSSzNZmB-hpx3AQADAgADbQADIAQ', 
                    'Сок Rich Вишня', 
                    '140 ₽', 
                    'RETURN_BACK_BE',
                    'ADDITION_BE4')
    
    elif call.data == '7.5':
        composition('AgACAgIAAxkBAAIYzGE98MqB-VaJqe7qvRFVUacWWmRoAAIbtzEb6vXwSbkuIcWBfFBEAQADAgADbQADIAQ', 
                    'Сок Rich Апельсин', 
                    '140 ₽', 
                    'RETURN_BACK_BE',
                    'ADDITION_BE5')
    
    elif call.data == '7.6':
        composition('AgACAgIAAxkBAAIYzWE98PE0zLCHwvAidltP6UR3zt2EAAIctzEb6vXwSeAGWG9AvCjYAQADAgADbQADIAQ', 
                    'Сок Rich Ананас', 
                    '140 ₽', 
                    'RETURN_BACK_BE',
                    'ADDITION_BE6')

    elif call.data == '7.7':
        composition('AgACAgIAAxkBAAIYzmE98cuvqhpvUNqOi_wtbSSg_8gAAyK3MRvq9fBJRBF_Zg2JncsBAAMCAANtAAMgBA', 
                    'Sprite\n0.5 литра', 
                    '80 ₽', 
                    'RETURN_BACK_BE',
                    'ADDITION_BE7')
   
    elif call.data == '7.8':
        composition('AgACAgIAAxkBAAIYz2E98ksNRIm_n19cOQ0X1NR8ClsCAAIjtzEb6vXwSYem0iqzRBPKAQADAgADbQADIAQ', 
                    'Sprite\n1.0 литр', 
                    '100 ₽', 
                    'RETURN_BACK_BE',
                    'ADDITION_BE8')

    elif call.data == '7.9':
        composition('AgACAgIAAxkBAAIY0GE98pwF7XUyOuBn0Z6Cevg-LBzlAAIltzEb6vXwSZhhL_Jd9j-cAQADAgADbQADIAQ', 
                    'Fanta\n0.5 литра', 
                    '80 ₽', 
                    'RETURN_BACK_BE',
                    'ADDITION_BE9')

    elif call.data == '710':
        composition('AgACAgIAAxkBAAIY0WE98qot6K9cAu9P_jDmJbtBDK6HAAImtzEb6vXwSbJ7pGVoil4YAQADAgADbQADIAQ', 
                    'Fanta\n1.0 литра', 
                    '100 ₽', 
                    'RETURN_BACK_BE',
                    'ADDITION_BE10')

    elif call.data == '7.11':
        composition('AgACAgIAAxkBAAIY0mE98x0JE1e-uyqHKdcczXloJZoOAAIntzEb6vXwSZtIVlcWvvRqAQADAgADbQADIAQ', 
                    'Coca-cola\n0.5 литра', 
                    '80 ₽', 
                    'RETURN_BACK_BE',
                    'ADDITION_BE11')

    elif call.data == '7.12':
        composition('AgACAgIAAxkBAAIY02E98yGM_4O0q43WGG1zUDsg-YvAAAIotzEb6vXwSSbuvHSlEYWGAQADAgADbQADIAQ', 
                    'Coca-cola\n1.0 литра', 
                    '100 ₽', 
                    'RETURN_BACK_BE',
                    'ADDITION_BE12')

    elif call.data == '7.13':
        composition('AgACAgIAAxkBAAIY1GE98yWywEGEftHrYLbIb0pJTmKtAAIptzEb6vXwSSoY3ZaUndJsAQADAgADbQADIAQ', 
                    'Coca-cola\n2.0 литра', 
                    '140 ₽', 
                    'RETURN_BACK_BE',
                    'ADDITION_BE13')






    if call.data == '8.1':
        composition('AgACAgIAAxkBAAIY7mE98_iQLLFnwos4-YYYZS9UZC3JAAIrtzEb6vXwSWE03AFE0296AQADAgADbQADIAQ', 
                    'Состав: соус барбекю, Грудка, ветчина, охотничьи колбаски, сыр, огурцы, лук', 
                    '185 ₽', 
                    'RETURN_BACK_KA',
                    'ADDITION_KA1')

    elif call.data == '8.2':
        composition('AgACAgIAAxkBAAIY_GFBbcbrmeHJVC50P8MwMjv_28YLAAJQsjEbc4ERSorLBz0z6pjDAQADAgADbQADIAQ', 
                    'Состав: соус томатный, томаты, перец, перец халапеньо, куриная грудка, сыр, лук, шампиньоны', 
                    '165 ₽', 
                    'RETURN_BACK_KA',
                    'ADDITION_KA2')
    
    elif call.data == '8.3':
        composition('AgACAgIAAxkBAAIY_WFBbgbxTIawEqLJXDIxOsS76ffXAAJRsjEbc4ERSmL2zrQ31RtnAQADAgADbQADIAQ', 
                    'Состав: сырный соус, Грудка, охотничьи колбаски, сыр, томаты, огурцы, лук', 
                    '175 ₽', 
                    'RETURN_BACK_KA',
                    'ADDITION_KA3')
    
    elif call.data == '8.4':
        composition('AgACAgIAAxkBAAIY_mFBbmLXJZK2sHuYvuZgGIBQLmhOAAJSsjEbc4ERSimsi5bWQb7mAQADAgADbQADIAQ', 
                    'Состав: соус Цезарь, пекинская капуста, Грудка, сыр, томаты', 
                    '145 ₽', 
                    'RETURN_BACK_KA',
                    'ADDITION_KA4')






    if call.data == '9.1':
        composition('AgACAgIAAxkBAAIZBGFBbvwsZ4Roeiu524eWX0LmdzXtAAJTsjEbc4ERSlPMhDjfl-SIAQADAgADbQADIAQ', 
                    'Состав: Чесночный соус, ананасы, сыр моцарелла, грудка копчённая, пекинская капуста\nОбщий вес: 270гр', 
                    '150 ₽', 
                    'RETURN_BACK_SAL',
                    'ADDITION_SAL1')

    elif call.data == '9.2':
        composition('AgACAgIAAxkBAAIZBmFBb_mEwcft2iBs5z2Bsu3nsyiEAAJVsjEbc4ERSjCtsawZY_PIAQADAgADbQADIAQ', 
                    'Состав: томаты чери, сыр пармезан, соус Цезарь, куриная грудка, пекинская капуста, сухари\nОбщий вес: 230гр', 
                    '150 ₽', 
                    'RETURN_BACK_SAL',
                    'ADDITION_SAL2')
    
    elif call.data == '9.3':
        composition('AgACAgIAAxkBAAIZBWFBb5lnlYH2BeVCF4yvK4ARA1n0AAJUsjEbc4ERSiltXmImD77SAQADAgADbQADIAQ', 
                    'Состав: маслины, орегано, томаты чери, лист салата, масло оливковое, бальзамический соус, огурец, перец, сыр Фета\nОбщий вес: 230гр', 
                    '150 ₽', 
                    'RETURN_BACK_SAL',
                    'ADDITION_SAL3')
    
    




    #Возвращение к общему списку товаров
    if call.data == 'RETURN_BACK_P':#После нажатия этой кнопки 
        PIZZA()#Показываем какие пиццы у нас есть
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)#Удаляем кнопки после нажатия этой

    if call.data == 'RETURN_BACK_SU':
        SUSHI()
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    if call.data == 'RETURN_BACK_SE':
        SETS()
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    if call.data == 'RETURN_BACK_SN':
        SNACKS()
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    if call.data == 'RETURN_BACK_SP':
        SPECIAL_OFFERS()
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    if call.data == 'RETURN_BACK_SA':
        SAUCES()
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    if call.data == 'RETURN_BACK_BE':
        BEVERAGES()  
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    if call.data == 'RETURN_BACK_KA':
        KALZONE()
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    if call.data == 'RETURN_BACK_SAL':
        SALADS() 
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)






#_______________________________________________________________________________________________________________\||_|_|_|_|_|_|_|_|_|_|_|__|_|_|_|_||_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|-
#_______________________________________________________________________________________________________________\||_|_|_|_|_|_|_|_|_|_|_|__|_|_|_|_||_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|-
#_______________________________________________________________________________________________________________\||_|_|_|_|_|_|_|_|_|_|_|__|_|_|_|_||_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|-



    

    #То что происходит если нажать на кнопки Добавить в корзину  
    if call.data == 'ADDITION_P1':
        p1 += 1#Количество товара
        suma += 1#Стоимость товара
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P2':
        p2 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_P3':
        p3 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P4':
        p4 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_P5':
        p5 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P6':
        p6 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P7':
        p7 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_P8':
        p8 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P9':
        p9 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_P10':
        p10 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P11':
        p11 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P12':
        p12 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_P13':
        p13 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P14':
        p14 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_P15':
        p15 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P16':
        p16 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P17':
        p17 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_P18':
        p18 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P19':
        p19 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_P20':
        p20 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P21':
        p21 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P22':
        p22 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_P23':
        p23 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P24':
        p24 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_P25':
        p25 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P26':
        p26 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P27':
        p27 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_P28':
        p28 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P29':
        p29 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_P30':
        p30 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P31':
        p31 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P32':
        p32 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P33':
        p33 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_P34':
        p34 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P35':
        p35 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_P36':
        p36 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P37':
        p37 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P38':
        p38 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_P39':
        p39 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_P40':
        p40 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно




    if call.data == 'ADDITION_SU1':
        su1 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SU2':
        su2 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SU3':
        su3 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_SU4':
        su4 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SU5':
        su5 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_SU6':
        su6 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SU7':
        su7 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_SU8':
        su8 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SU9':
        su9 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно


    elif call.data == 'ADDITION_SU10':
        su10 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SU11':
        su11 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_SU12':
        su12 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SU13':
        su13 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно





    if call.data == 'ADDITION_SE1':
        se1 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SE2':
        se2 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SE3':
        se3 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_SE4':
        se4 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SE5':
        se5 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_SE6':
        se6 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SE7':
        se7 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_SE8':
        se8 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SE9':
        se9 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно






    if call.data == 'ADDITION_SN1':
        sn1 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SN2':
        sn2 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SN3':
        sn3 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно







    if call.data == 'ADDITION_SP1':
        sp1 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SP2':
        sp2 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SP3':
        sp3 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_SP4':
        sp4 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SP5':
        sp5 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_SP6':
        sp6 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SP7':
        sp7 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_SP8':
        sp8 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SP9':
        sp9 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно


    elif call.data == 'ADDITION_SP10':
        sp10 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SP11':
        sp11 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_SP12':
        sp12 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SP13':
        sp13 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно







    if call.data == 'ADDITION_SA1':
        sa1 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SA2':
        sa2 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SA3':
        sa3 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_SA4':
        sa4 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SA5':
        sa5 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно









    if call.data == 'ADDITION_BE1':
        be1 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_BE2':
        be2 = be2 + 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_BE3':
        be3 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_BE4':
        be4 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_BE5':
        be5 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_BE6':
        be6 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_BE7':
        be7 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_BE8':
        be8 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_BE9':
        be9 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно


    elif call.data == 'ADDITION_BE10':
        be10 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_BE11':
        be11 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_BE12':
        be12 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_BE13':
        be13 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно







    if call.data == 'ADDITION_KA1':
        ka1 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_KA2':
        ka2 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_KA3':
        ka3 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_KA4':
        ka4 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       



    if call.data == 'ADDITION_SAL1':
        sal1 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно

    elif call.data == 'ADDITION_SAL2':
        sal2 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно
       
    elif call.data == 'ADDITION_SAL3':
        sal3 += 1
        suma += 1
        bot.answer_callback_query(callback_query_id=call.id, text='Хей хороший выбор')#Всплывающее окно






    #То что происходит если нажать на кнопку Купить (выбираем адрес доставки или меняем его)
    if call.data == '0.4':
        global address_d1
        global address_d2
        global address_d3
        db = sqlite3.connect('pizza_shops.db')#Создаём базу данных которая и подключаемся к ней
        sql = db.cursor()

        
        
        
        #У каждого пользователя может быть до 3 адресов, здесь вы вытаскиваем эти 3 адреса из базы данных
        sql.execute(f"SELECT address01 FROM users WHERE username = '{call.from_user.username}'")#Берём определённую ячейку из таблицы (адрес), ищем по username
        address_d1 = sql.fetchone()#Засовываем адрес в переменную

        sql.execute(f"SELECT address02 FROM users WHERE username = '{call.from_user.username}'")
        address_d2 = sql.fetchone()

        sql.execute(f"SELECT address03 FROM users WHERE username = '{call.from_user.username}'")
        address_d3 = sql.fetchone()

     
        markup = telebot.types.InlineKeyboardMarkup()#
        markup.add(telebot.types.InlineKeyboardButton(text=str(address_d1), callback_data='address_p1'))#Кнопки для выбора адреса доставки
        markup.add(telebot.types.InlineKeyboardButton(text=str(address_d2), callback_data='address_p2'))
        markup.add(telebot.types.InlineKeyboardButton(text=str(address_d3), callback_data='address_p3'))
        markup.add(telebot.types.InlineKeyboardButton(text='Записать новый адрес, или поменять старый', callback_data='address_p55'))#Кнопка для замены адреса

        bot.send_message(call.message.chat.id, 'Выберите адрес. На который курьер доставит ваш заказ', reply_markup=markup)#Сообщение к которому всё прекреплено

        
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    



    def receipt(ad):
        api_access_token = 'FFFFFFFFFFFFFFFFFFFFFFF' #Токен кошелька (можно получить здесь https://qiwi.com/api)
        phone = "88888888888"#Телефон кошелька

        comment_i = str(randint(100000, 999999))#Генерируем код

        bot.send_message(call.message.chat.id, f"'Был выбран адрес'{ad}")
        bot.send_message(call.message.chat.id, f"'Итоговая сумма'{suma}' руб.")#Выводим общюю суммы покупок


        bot.send_message(call.message.chat.id, f"Переведите {suma} рублей на QIWI счет '{phone}'\n С коментарием: ")
        bot.send_message(call.message.chat.id, f"{comment_i}")

        tir = 0

        for i in range (12):#Главный цикл
            if tir == 1:#Проверяем можем ли остановить цикл
                break

            s = requests.Session()
            s.headers['authorization'] = 'Bearer ' + api_access_token  
            h = s.get('https://edge.qiwi.com//payment-history/v2/persons/88888888888/payments?rows=3&operation=IN&sources%5B0%5D=QW_RUB&sources%5B1%5D=CARD ')
            a = json.loads(h.text)#В переменной хранится информация о переводах в виде словаря в котором можно копатся

            f = 0
            for i in range (3):#второй цикл

                #Вытаскивам из переменной то что нам нужно
                dd = a['data']
                ss = dd[f]#Вытаскиваем конкретный элемент (инф. об одном платеже)
                aa = ss['comment']#Вытаскиваем коментарий прикреплённый к платежу
                    
                #Вытаскиваем сумму
                aa1= ss['sum']
                aa2 = aa1['amount']

                #Проверяем 
                if aa == comment_i:#Проверяем коментарий 
                    if aa2 == suma:#Проверяем сумму
                        
                        bot.send_message(call.message.chat.id, f"Платёж получен! Ждите курьера, по адресу {ad}")

                        asd = str(ad)#Берём адрес
                        goods_db(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, 
                        p21, p22, p23, p24, p25, p26, p27, p28 , p29, p30, p31, p32, p33, p34, p35, p36, p37, p38, p39, p40, 
                        su1, su2, su3, su4, su5, su6, su7, su8, su9, su10, su11 , su12, su13, 
                        se1, se2, se3, se4, se5, se6, se7, se8, se9, 
                        sn1, sn2, sn3, 
                        sp1, sp2, sp3, sp4, sp5, sp6, sp7, sp8, sp9, sp10, sp11, sp12, sp13, 
                        sa1, sa2, sa3, sa4, sa5, 
                        be1, be2, be3, be4, be5, be6, be7, be8, be9, be10, be11, be12, be13, 
                        ka1, ka2, ka3, ka4, 
                        sal1, sal2, sal3, asd)#Записываем информацию о покупке в базу данных
                

                        tir = 1#Говорим что пора выключать главный цикл ибо цель достигнута
                        break

                    
                    
                f = f + 1#Меняем значение переменной чтоба с каждой итерацией второго цикла брать новый элемент переменной "a" (инф. о следующем платеже)
                
            if tir == 0:#Это нужно чтобы после того как оплата пройдёт не ждать 20 секунд и остановить цикл
                print(20)
                time.sleep(20)#ждём 20секунд и снова вытаскиваем информацию о платежах


   
    
    
        

    #То что происходит если нажать на кнопку выбор адреса для покупки
    if call.data == 'address_p1':
        receipt(address_d1)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)#Удаляем кнопки после нажатия этой



    elif call.data == 'address_p2':
        receipt(address_d2)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

        
    
    elif call.data == 'address_p3':
        receipt(address_d3)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        
    
    
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    #Обнуляем корзину
    if call.data == '0.5':
        p1 = 0
        p2 = 0
        p3 = 0

        p4 = 0
        p5 = 0
        p6 = 0
        p7 = 0
        p8 = 0
        p9 = 0
        p10 = 0
        p11 = 0
        p12 = 0
        p13 = 0
        p14 = 0
        p15 = 0
        p16 = 0
        p17 = 0
        p18 = 0
        p19 = 0
        p20 = 0
        p21 = 0
        p22 = 0
        p23 = 0
        p24 = 0
        p25 = 0
        p26 = 0
        p27 = 0
        p28 = 0
        p29 = 0
        p30 = 0
        p31 = 0
        p32 = 0
        p33 = 0
        p34 = 0
        p35 = 0
        p36 = 0
        p37 = 0
        p38 = 0
        p39 = 0
        p40 = 0

        su1 = 0
        su2 = 0
        su3 = 0
        su4 = 0
        su5 = 0
        su6 = 0
        su7 = 0
        su8 = 0
        su9 = 0
        su10 = 0
        su11 = 0
        su12 = 0
        su13 = 0

        se1 = 0
        se2 = 0
        se3 = 0
        se4 = 0
        se5 = 0
        se6 = 0
        se7 = 0
        se8 = 0
        se9 = 0

        sn1 = 0
        sn2 = 0
        sn3 = 0

        sp1 = 0
        sp2 = 0
        sp3 = 0
        sp4 = 0
        sp5 = 0
        sp6 = 0
        sp7 = 0
        sp8 = 0
        sp9 = 0
        sp10 = 0
        sp11 = 0
        su12 = 0
        sp13 = 0

        sa1 = 0
        sa2 = 0
        sa3 = 0
        sa4 = 0
        sa5 = 0
        sa6 = 0

        be1 = 0
        be2 = 0
        be3 = 0
        be4 = 0
        be5 = 0
        be6 = 0
        be7 = 0
        be8 = 0
        be9 = 0
        be10 = 0
        be11 = 0
        be12 = 0
        be13 = 0

        ka1 = 0
        ka2 = 0
        ka3 = 0
        ka4 = 0

        sal1 = 0
        sal2 = 0
        sal3 = 0

        suma = 0
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)#Удаляем кнопки 
        bot.answer_callback_query(callback_query_id=call.id, text='Корзина очищена')


    #______________________________________________________________________________________________________________________________

    #Это сработает если мы нажали на кнопку поменять адрес
    if call.data == 'address_p55':
        db = sqlite3.connect('pizza_shops.db')#Создаём базу данных и подключаемся к ней
        sql = db.cursor()

        #Вытаскиваем адреса из таблицы чтобы потом подставить  их в качестве названия кнопок
        sql.execute(f"SELECT address01 FROM users WHERE username = '{call.from_user.username}'")
        address_d1 = sql.fetchone()

        sql.execute(f"SELECT address02 FROM users WHERE username = '{call.from_user.username}'")
        address_d2 = sql.fetchone()

        sql.execute(f"SELECT address03 FROM users WHERE username = '{call.from_user.username}'")
        address_d3 = sql.fetchone()
        
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text=str(address_d1), callback_data='address_p-1'))#Кнопка для замены первого адреса
        markup.add(telebot.types.InlineKeyboardButton(text=str(address_d2), callback_data='address_p-2'))#Кнопка для замены второго адреса
        markup.add(telebot.types.InlineKeyboardButton(text=str(address_d3), callback_data='address_p-3'))#Кнопка для замены третьего адреса
        

        bot.send_message(call.message.chat.id, 'Какой из адресов выбы хотели поменять', reply_markup=markup)
        
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    

    
    #Берём информацию у пользователя и заменяем первый адрес
    if call.data == 'address_p-1':
        def start_2(message):
            
            tra = message.text#засовываем в переменную то что написал пользователь
            bot.send_message(call.message.chat.id, tra,)#
            change1(tra, call.from_user.username)#Функция для замены первого адреса
        
        msg = bot.send_message(call.message.chat.id, 'Напишите новый адрес')#Просим пользователя написать новый адрес
        bot.register_next_step_handler(msg, start_2)#Берём информацию у пользователя
        
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    
    #Берём информацию у пользователя и заменяем второй адрес
    elif call.data == 'address_p-2':
        def start_2(message):
            
            tra = message.text
            bot.send_message(call.message.chat.id, tra,)
            change2(tra, call.from_user.username)#функция для замены второго адреса
        
        msg = bot.send_message(call.message.chat.id, 'Напишите новый адрес')#
        bot.register_next_step_handler(msg, start_2)
        
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        
    #Берём информацию у пользователя и заменяем третий адрес
    elif call.data == 'address_p-3':
        def start_2(message):
            
            tra = message.text
            bot.send_message(call.message.chat.id, tra,)
            change3(tra, call.from_user.username)#Функция для замены третьего адреса
        
        msg = bot.send_message(call.message.chat.id, 'Напишите новый адрес')
        bot.register_next_step_handler(msg, start_2)

        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    


bot.polling(none_stop = True)









