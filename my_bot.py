import os
import threading
from flask import Flask
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Создаем Flask-приложение
flask_app = Flask(__name__)
port = int(os.environ.get('PORT', 3000))  # Render задаёт порт через переменную окружения PORT

@flask_app.route('/')
def home():
    return f"Сервер прослушивает порт {port}"

# Токен вашего бота
TOKEN = "7568589896:AAF6WNjcbv0JoKujy44DsG3RtAe78JE57pU"

# --- Telegram Bot Handlers ---

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Қазақша", "Русский"],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text(
        f"Қайырлы күн / Добрый день, {update.effective_user.first_name}! Қош келдіңіз/Добро пожаловать!\n"
        "Вас приветствует Генеральное консульство Республики Казахстан в городе Пусан.\n"
        "Чем мы можем вам помочь?",
        reply_markup=reply_markup
    )

# Обработчик для меню на казахском языке
async def kazakh_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Консулдық мәселелер"],
        ["Жұмыс уақыты"],
        ["Өтініш нысандары"],
        ["Жиі қойылатын сұрақтар"],
        ["Байланыс ақпараты"],
        ["Бастапқы бетке оралу", "қаз/рус"],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Тілді таңдадыңыз: Қазақша", reply_markup=reply_markup)

# Обработчик для меню на русском языке
async def russian_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Консульские вопросы"],
        ["Время работы"],
        ["Шаблоны заявлений"],
        ["Часто задаваемые вопросы"],
        ["Контакты"],
        ["Вернуться в главное меню", "қаз/рус"],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Вы выбрали язык: Русский", reply_markup=reply_markup)

# Обработчик текстовых сообщений от пользователей
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Қазақша":
        await kazakh_menu(update, context)
    elif text == "Русский":
        await russian_menu(update, context)
    elif text == "қаз/рус":
        await start(update, context)
    else:
        await update.message.reply_text("Пожалуйста, выберите одну из доступных опций.")

# --- Функция для запуска Telegram-бота ---
def run_bot():
    bot_app = ApplicationBuilder().token(TOKEN).build()
    bot_app.add_handler(CommandHandler("start", start))
    bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Бот запущен! Нажмите Ctrl+C для остановки.")
    bot_app.run_polling(drop_pending_updates=True)

# --- Основной блок ---
if __name__ == "__main__":
    # Запускаем Telegram-бота в отдельном потоке
    threading.Thread(target=run_bot, daemon=True).start()
    # Запускаем Flask-сервер в главном потоке
    flask_app.run(host='0.0.0.0', port=port)
