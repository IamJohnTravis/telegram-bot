from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder
import asyncio

app = Flask(__name__)
TOKEN = os.getenv("TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

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
@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(), bot_app.bot)
    asyncio.run(bot_app.process_update(update))  # Используем asyncio.run()
    return "OK"

# Запуск Webhook
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot_app.bot.setWebhook(f"{WEBHOOK_URL}/webhook"))
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
