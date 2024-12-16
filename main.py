import sqlite3
import telebot
from telebot import types

conn=sqlite3.connect("C:/BD/tg.db", check_same_thread=False)
cur = conn.cursor()

bot = telebot.TeleBot('8058602209:AAFgcu6bXsWB5xsaFTHMVHDV1LVu06xOxnQ')

@bot.message_handler(commands=['start'])
def menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    australia = types.KeyboardButton("Австралия")
    africa = types.KeyboardButton("Африка")
    evrasia = types.KeyboardButton("Евразия")
    namerika = types.KeyboardButton("Северная Америка")
    samerika = types.KeyboardButton("Южная Америка")
    keyboard.add(australia, africa, evrasia, namerika, samerika)
    bot.send_message(message.chat.id, text='Привет, я бот который предоставляет информацию о странах, сначала выбери континент', reply_markup=keyboard)

@bot.message_handler(content_types="web_app_data") #получаем отправленные данные 
def answer(webAppMes):
   data = json.loads(webAppMes.web_app_data.data)
   print(webAppMes.web_app_data.data) #конкретно то что мы передали в бота
   bot.send_message(webAppMes.chat.id, "Кнопка отреагировала на клик:")
   bot.send_message(webAppMes.chat.id, data)

@bot.message_handler(content_types=['text'])
def callback_worker(message):
    if message.text == "Австралия":
        australiainfo = conn.execute('Select Информация from Австралия WHERE id ==1').fetchone()
        bot.send_message(message.chat.id, australiainfo)

    elif message.text == "Африка":
        africa_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        africa_menu.add('Алжир', 'Гвинея', 'Египет', 'Зимбабве', 'Южный Судан')
        bot.send_message(message.chat.id, 'Выбери страну', reply_markup=africa_menu)

    elif message.text == "Алжир":
        aljir = conn.execute('Select Информация from Африка WHERE id == 1').fetchone()
        bot.send_message(message.chat.id, aljir)
    elif message.text == "Египет":
        egipet = conn.execute('Select Информация from Африка WHERE id == 2').fetchone()
        bot.send_message(message.chat.id, egipet)
    elif message.text == "Гвинея":
        gvineya = conn.execute('Select Информация from Африка WHERE id == 3').fetchone()
        bot.send_message(message.chat.id, gvineya)
    elif message.text == "Зимбабве":
        zimbabve = conn.execute('Select Информация from Африка WHERE id == 4').fetchone()
        bot.send_message(message.chat.id, zimbabve)
    elif message.text == "Южный Судан":
        sudan = conn.execute('Select Информация from Африка WHERE id == 5').fetchone()
        bot.send_message(message.chat.id, sudan)

    elif message.text == "Евразия":
        evrasia_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        evrasia_menu.add('Япония', 'Китай', ' Финляндия', 'Украина', 'Беларусь', 'Казахстан', 'Россия')
        bot.send_message(message.chat.id, 'Выбери страну', reply_markup=evrasia_menu)

    elif message.text == "Япония":
        japan = conn.execute('Select Информация from Евразия WHERE id == 1').fetchone()
        bot.send_message(message.chat.id, japan)
    elif message.text == "Китай":
        china = conn.execute('Select Информация from Евразия WHERE id == 2').fetchone()
        bot.send_message(message.chat.id, china)
    elif message.text == "Финляндия":
        finland = conn.execute('Select Информация from Евразия WHERE id == 3').fetchone()
        bot.send_message(message.chat.id, finland)
    elif message.text == "Украина":
        ukraine = conn.execute('Select Информация from Евразия WHERE id == 4').fetchone()
        bot.send_message(message.chat.id, ukraine)
    elif message.text == "Беларусь":
        belarus = conn.execute('Select Информация from Евразия WHERE id == 5').fetchone()
        bot.send_message(message.chat.id, belarus)
    elif message.text == "Казахстан":
        kazahstan = conn.execute('Select Информация from Евразия WHERE id == 6').fetchone()
        bot.send_message(message.chat.id, kazahstan)
    elif message.text == "Россия":
        russia = conn.execute('Select Информация from Евразия WHERE id == 7').fetchone()
        bot.send_message(message.chat.id, russia)

    elif message.text == "Северная Америка":
        namerika_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        namerika_menu.add('США', 'Канада', ' Мексика')
        bot.send_message(message.chat.id, 'Выбери страну', reply_markup=namerika_menu)

    elif message.text == "США":
        usa = conn.execute('Select Информация from СевернаяАмерика WHERE id == 1').fetchone()
        bot.send_message(message.chat.id, usa)
    elif message.text == "Канада":
        canada = conn.execute('Select Информация from СевернаяАмерика WHERE id == 2').fetchone()
        bot.send_message(message.chat.id, canada)
    elif message.text == "Мексика":
        mexico = conn.execute('Select Информация from СевернаяАмерика WHERE id == 3').fetchone()
        bot.send_message(message.chat.id, mexico)

    elif message.text == "Южная Америка":
        samerika_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        samerika_menu.add('Бразилия', 'Аргентина', 'Перу', 'Чили')
        bot.send_message(message.chat.id, 'Выбери страну', reply_markup=samerika_menu)

    elif message.text == "Бразилия":
        brasilia = conn.execute('Select Информация from ЮжнаяАмерика WHERE id == 1').fetchone()
        bot.send_message(message.chat.id, brasilia)
    elif message.text == "Аргентина":
        argentina = conn.execute('Select Информация from ЮжнаяАмерика WHERE id == 2').fetchone()
        bot.send_message(message.chat.id, argentina)
    elif message.text == "Перу":
        peru = conn.execute('Select Информация from ЮжнаяАмерика WHERE id == 3').fetchone()
        bot.send_message(message.chat.id, peru)
    elif message.text == "Чили":
        chili = conn.execute('Select Информация from ЮжнаяАмерика WHERE id == 4').fetchone()
        bot.send_message(message.chat.id, chili)

    elif message.text == "Главное меню":
        menu(message)

bot.polling(none_stop=True, interval=0)
