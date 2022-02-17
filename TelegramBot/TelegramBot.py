import telebot

TOKEN = "5165341256:AAFTgeuo_RSYLuUl3nxPEh-DN7HEdMp8kws"

bot = telebot.TeleBot(TOKEN)


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, {message.chat.username}")


# Обрабатывается все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass


# Обрабатываются все текстовые сообщения
@bot.message_handler(content_types=['text'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Рано ложиться и рано вставать — вот что делает человека здоровым, богатым и умным.")


# Обрабатываются все текстовые сообщения
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, "Nice meme XDD")


bot.polling(none_stop=True)
