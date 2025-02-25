import os
import threading
import asyncio
from flask import Flask
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
)

# Создаем Flask-приложение
flask_app = Flask(__name__)
port = int(os.environ.get('PORT', 3000))  # Render задает порт через переменную окружения PORT

@flask_app.route('/')
def home():
    return f"Сервер прослушивает порт {port}"

# Токен вашего бота
TOKEN = "7568589896:AAF6WNjcbv0JoKujy44DsG3RtAe78JE57pU"

# --- Обработчики Telegram-бота ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Қазақша", "Русский"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text(
        f"Қайырлы күн / Добрый день, {update.effective_user.first_name}! Қош келдіңіз/Добро пожаловать!\n"
        "Вас приветствует Генеральное консульство Республики Казахстан в городе Пусан.\n"
        "Чем мы можем вам помочь?",
        reply_markup=reply_markup
    )

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
        await
