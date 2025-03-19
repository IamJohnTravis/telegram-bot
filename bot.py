import os
import asyncio
from flask import Flask, request
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Загружаем переменные окружения
TOKEN = os.getenv("TOKEN")  
WEBHOOK_URL = os.getenv("https://telegram-bot-yvu3.onrender.com")  # Например: "https://your-bot.onrender.com"

# Создаем Flask-приложение
app = Flask(__name__)

# Инициализация бота
bot_app = ApplicationBuilder().token(TOKEN).build()

# Функция обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Қазақша", "Русский"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text("Қайырлы күн / Добрый день! Чем можем помочь?", reply_markup=reply_markup)

# Функция обработки выбора языка
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Қазақша":
        await update.message.reply_text("Вы выбрали казахский язык.")
    elif text == "Русский":
        await update.message.reply_text("Вы выбрали русский язык.")
    else:
        await update.message.reply_text("Выберите доступную опцию.")

# Добавляем обработчики команд
bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Главная страница (Render требует открытую страницу)
@app.route("/", methods=["GET"])
def home():
    return "Бот работает!"

# Webhook для Telegram
@app.route(f"/{TOKEN}", methods=["POST"])
async def webhook():
    update = Update.de_json(request.get_json(), bot_app.bot)
    await bot_app.process_update(update)
    return "OK"

# Запуск Webhook
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot_app.bot.setWebhook(f"{WEBHOOK_URL}/{TOKEN}"))
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
