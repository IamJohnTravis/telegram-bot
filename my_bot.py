import os
import asyncio
from flask import Flask, request
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Загружаем токен бота и URL Webhook из переменных окружения
TOKEN = os.getenv("7568589896:AAGfc9UP9ePvk4NB_LmpmnjCcbm2Hj03OQ8")  
WEBHOOK_URL = os.getenv("https://telegram-bot-yvu3.onrender.com")

# Создаем Flask-приложение
app = Flask(__name__)

# Инициализация Telegram-бота
bot_app = ApplicationBuilder().token(TOKEN).build()

# Функция обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Қазақша", "Русский"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

    await update.message.reply_text(
        f"Қайырлы күн  / Добрый день, {update.effective_user.first_name}! Қош келдіңіз/Добро пожаловать! \n"
        "Вас приветствует Генеральное консульство Республики Казахстан в городе Пусан.\n"
        "Чем мы можем вам помочь?",
        reply_markup=reply_markup
    )

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

# Запуск приложения
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot_app.bot.setWebhook(f"{WEBHOOK_URL}/{TOKEN}"))
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
