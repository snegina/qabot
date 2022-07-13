#библиотеки, которые загружаем из вне
import telebot
TOKEN = '5401407303:AAGfN0UnHquDmxeeP75F4MtWaPM__q0urag'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcom.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("👉Follow my github")
	item2 = types.KeyboardButton("✍️Write message")
	item3 = types.KeyboardButton("▶️Youtube")

	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, "Привет, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '👉Follow my github':
			bot.send_message(message.chat.id, 'https://github.com/snegina')
		elif message.text == '✍️Write message':
			bot.send_message(message.chat.id, 'http://t.me/snegina')
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить😢')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods