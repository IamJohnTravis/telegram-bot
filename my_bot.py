import os
import asyncio
from flask import Flask, request
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Получаем переменные окружения
TOKEN = os.getenv("7568589896:AAGfc9UP9ePvk4NB_LmpmnjCcbm2Hj03OQ8")  # Токен Telegram-бота
WEBHOOK_URL = os.getenv("https://telegram-bot-yvu3.onrender.com")  # URL Render для Webhook

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

# Функция отображения меню на казахском языке
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

# Функция отображения меню на русском языке
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

# Функция обработки выбора пользователя
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Қазақша":
        await kazakh_menu(update, context)
    elif text == "Русский":
        await russian_menu(update, context)
    elif text == "қаз/рус":
        await start(update, context)
    elif text == "Консулдық мәселелер":
        await update.message.reply_text("Консулдық мәселелер туралы толық ақпарат: https://www.gov.kz/memleket/entities/mfa-busan/activities/58636?lang=ru")
    elif text == "Жұмыс уақыты":
        await update.message.reply_text("Консульский отдел работает с 9:30 до 12:30 и с 16:00 до 17:00, кроме среды.")
    elif text == "Байланыс ақпараты":
        await update.message.reply_text("Контакты консульства: +(82 51) 466 7001\nОфициальный сайт: https://www.gov.kz/memleket/entities/mfa-busan")
    elif text == "Консульские вопросы":
        await update.message.reply_text("Консульские вопросы: https://www.gov.kz/memleket/entities/mfa-busan/activities/58636?lang=ru")
    elif text == "Время работы":
        await update.message.reply_text("Прием посетителей по консульским вопросам осуществляется в понедельник, вторник, четверг и пятницу с 9.30 до 12.30 ч., выдача готовых документов с 16.00 до 17.00 ч.")
    elif text == "Шаблоны заявлений":
        await update.message.reply_text("Шаблоны заявлений: https://www.gov.kz/memleket/entities/mfa-busan/documents/details/753610?lang=ru")
    elif text == "Контакты":
        await update.message.reply_text("Генеральное консульство Республики Казахстан в г. Пусан: +(82 51) 466 7001")
    elif text == "Вернуться в главное меню":
        await russian_menu(update, context)
    elif text == "Бастапқы бетке оралу":
        await kazakh_menu(update, context)
    else:
        await update.message.reply_text("Пожалуйста, выберите одну из доступных опций.")

# Добавляем обработчики команд
bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Главная страница (чтобы Render не выключал сервер)
@app.route("/", methods=["GET"])
def home():
    return "Бот работает!"

# Эндпоинт Webhook для Telegram
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
