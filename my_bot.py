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

# Функция для обработки текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Қазақша":
        await kazakh_menu(update, context)
    elif text == "Русский":
        await russian_menu(update, context)
    else:
        await update.message.reply_text("Извините, я не понимаю эту команду.")

# Функция для меню на казахском языке
async def kazakh_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Байланыс ақпараты", "Консулдық мәселелер"],
        ["Жұмыс уақыты", "Өтініш нысандары"],
        ["Бастапқы бетке оралу"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Сіз Қазақ тілін таңдадыңыз. Төмендегі мәзірден таңдаңыз:", reply_markup=reply_markup)

# Функция для меню на русском языке
async def russian_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Контакты", "Консульские вопросы"],
        ["Время работы", "Шаблоны заявлений"],
        ["Вернуться в главное меню"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Вы выбрали Русский язык. Пожалуйста, выберите пункт меню:", reply_markup=reply_markup)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    # Добавляем обработчики команд и сообщений
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

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
