import telebot
from telebot import types

token = '7000352105:AAE6lRX_3sf-a0BFyFObBQ3j9_Izdo36RKI'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton('Button 1')
    button2 = types.KeyboardButton('Button 2')
    markup.add(button1, button2)
    bot.reply_to(message, "Виберіть кнопку:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == 'Button 1':
        bot.reply_to(message, "Ви натиснули кнопку 1")
    elif message.text == 'Button 2':
        bot.reply_to(message, "Ви натиснули кнопку 2")
    else:
        bot.reply_to(message, "Будь ласка, виберіть кнопку з клавіатури.")

@bot.message_handler(commands=['hide_keyboard'])
def hide_keyboard(message):
    markup = types.ReplyKeyboardRemove()
    bot.reply_to(message, "Клавіатура прибрана.", reply_markup=markup)

bot.polling()


Лістинг коду:   2
import telebot
from telebot import types

token = '7000352105:AAE6lRX_3sf-a0BFyFObBQ3j9_Izdo36RKI'

bot = telebot.TeleBot(token)


button_clicks = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton("Button 1", callback_data='button1')
    button2 = types.InlineKeyboardButton("Button 2", callback_data='button2')
    button3 = types.InlineKeyboardButton("Button 3", callback_data='button3')
    markup.add(button1, button2, button3)
    bot.reply_to(message, "Виберіть кнопку:", reply_markup=markup)

    button_clicks[message.chat.id] = 0

@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    user_id = call.message.chat.id
    button_clicks[user_id] += 1
    if call.data == 'button1':
        bot.send_message(user_id, "Ви натиснули кнопку 1")
    elif call.data == 'button2':
        bot.send_message(user_id, "Ви натиснули кнопку 2")
    elif call.data == 'button3':
        bot.send_message(user_id, "Ви натиснули кнопку 3")
    # Перевірка та видалення
    if button_clicks[user_id] >= 3:
        markup = types.ReplyKeyboardRemove()
        bot.send_message(user_id, "Клавіатура прибрана.", reply_markup=markup)

        button_clicks[user_id] = 0

bot.polling()
