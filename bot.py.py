import telebot
from telebot import types

# Введіть свій токен
API_TOKEN = '6823324629:AAHXxhIjknsrJeWiZRpV69MzEVhLbmBIyjI'

# Створення бота
bot = telebot.TeleBot(823324629:AAHXxhIjknsrJeWiZRpV69MzEVhLbmBIyjI)

# Обробка команди /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Я ваш бот. Як можу допомогти?")

# Обробка команди /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Я можу виконувати наступні команди:\n"
        "/start - Почати роботу зі мною\n"
        "/help - Отримати список команд\n"
        "Просто напишіть мені повідомлення, і я відповім!"
    )
    bot.reply_to(message, help_text)

# Обробка звичайних повідомлень
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, f"Ви сказали: {message.text}")

# Запуск бота
bot.polling()
