from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

# Токен вашего бота
TOKEN = "7568589896:AAF6WNjcbv0JoKujy44DsG3RtAe78JE57pU"

# Порт для работы вебхуков
PORT = int(os.environ.get("PORT", 8443))

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Қазақша", "Русский"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        f"Қайырлы күн/Добрый день, {update.effective_user.first_name}! Қош келдіңіз/Добро пожаловать! "
        "Вас приветствует Генеральное консульство Республики Казахстан в городе Пусан.\n"
        "Чем мы можем вам помочь?",
        reply_markup=reply_markup
    )

# Добавьте остальные функции меню здесь (kazakh_menu, russian_menu и т.д.)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    # Добавляем обработчики команд и сообщений
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  # handle_message нужно реализовать

    # Настройка вебхука
    WEBHOOK_URL = f"https://telegram-bot-4-my1j.onrender.com/{TOKEN}"

    async def start_webhook():
        # Устанавливаем вебхук
        await app.bot.set_webhook(url=WEBHOOK_URL)

        # Запускаем приложение с вебхуком
        app.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=TOKEN
        )

    # Запускаем асинхронный вебхук
    import asyncio
    asyncio.run(start_webhook())
