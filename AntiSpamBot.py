import telebot

# Создаем объект бота
bot = telebot.TeleBot("YOUR_TOKEN")

# Список стоп-слов
with open('stop_words.txt', 'r') as f:
    stop_words = [line.strip() for line in f]

# Обработчик сообщений
@bot.message_handler(func=lambda message: any(word in message.text.lower() for word in stop_words))
def handle_spam(message):
    # Удаляем сообщение
    bot.delete_message(message.chat.id, message.message_id)
    # Баним пользователя
    bot.kick_chat_member(message.chat.id, message.from_user.id)

# Запускаем бота
bot.polling(none_stop=True)
