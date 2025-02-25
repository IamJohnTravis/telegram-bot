import requests
import threading
import asyncio
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import time
import os
from flask import Flask

# Создаём Flask-сервер
flask_app = Flask(__name__)
port = int(os.environ.get('PORT', 3000))  # Render задаёт порт через переменную окружения PORT

@flask_app.route('/')
def home():
    return f"Сервер прослушивает порт {port}"

# Токен вашего бота и URL для восстановления сервиса
TOKEN = "7568589896:AAF6WNjcbv0JoKujy44DsG3RtAe78JE57pU"
RENDER_RESTART_URL = "https://api.render.com/deploy/srv-cu8tv3i3esus739soco0?key=1ITZYdIhpPI"

def check_service():
    try:
        # Здесь замените URL на нужный, например, если хотите проверить именно свой веб-сервис:
        response = requests.get("https://telegram-bot-yvu3.onrender.com", timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def restart_service():
    try:
        response = requests.get(RENDER_RESTART_URL)
        if response.status_code == 200:
            print("Сервис успешно перезапущен.")
        else:
            print(f"Ошибка при перезапуске сервиса: {response.status_code}")
    except requests.RequestException as e:
        print(f"Не удалось выполнить запрос на перезапуск: {e}")

# Асинхронный обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Получена команда /start")
    if not check_service():
        restart_service()
    keyboard = [["Қазақша", "Русский"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text(
        f"Қайырлы күн / Добрый день, {update.effective_user.first_name}! Қош келдіңіз/Добро пожаловать!\n"
        "Вас приветствует Генеральное консульство Республики Казахстан в городе Пусан.\n"
        "Чем мы можем вам помочь?",
        reply_markup=reply_markup
    )

# Пример обработчиков для меню (аналогично вашим функциям)
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

def monitor_service():
    while True:
        if not check_service():
            print("Сервис недоступен. Перезапускаю...")
            restart_service()
        time.sleep(300)

# Асинхронная функция для запуска бота
async def run_bot():
    bot_app = ApplicationBuilder().token(TOKEN).build()
    bot_app.add_handler(CommandHandler("start", start))
    bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    threading.Thread(target=monitor_service, daemon=True).start()
    print("Бот запущен! Нажмите Ctrl+C для остановки.")
    # drop_pending_updates=True – чтобы сбросить старые обновления
    await bot_app.run_polling(drop_pending_updates=True)

def run_flask():
    flask_app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    # Запускаем Flask-сервер в отдельном потоке, чтобы Render видел открытый порт
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    # Запускаем Telegram-бота в основном потоке с корректным event loop
    asyncio.run(run_bot())
