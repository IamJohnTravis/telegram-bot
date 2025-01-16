from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Токен вашего бота
TOKEN = "7568589896:AAF6WNjcbv0JoKujy44DsG3RtAe78JE57pU"

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Кнопки для клавиатуры
    keyboard = [
        ["1 Часто задаваемые вопросы"],  # Первая строка кнопок
        ["2 Контакты"],  # Вторая строка кнопок
        ["3 Назад в главное меню"],  # Третья строка кнопок
    ]

    # Создаём клавиатуру
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    # Отправляем сообщение с кнопками
    await update.message.reply_text(
        f"Добрый день, {update.effective_user.first_name}! Добро пожаловать! Вас приветствует Генеральное консульство Республики Казахстан в городе Пусан\n"
        "Чем мы можем вам помочь?",
        reply_markup=reply_markup
    )

# Функция для обработки выбора пользователя
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "1 Часто задаваемые вопросы":
        await update.message.reply_text("Вы выбрали 'Часто задаваемые вопросы'. Вот что я могу рассказать...")
    elif text == "2 Контакты":
        # Отправляем ссылку на официальный сайт
        await update.message.reply_text(
            "Вот ссылка на наш официальный сайт:\n"
            "https://www.gov.kz/memleket/entities/mfa-busan"
        )
    elif text == "3 Назад в главное меню":
        await start(update, context)  # Возвращаемся к меню
    else:
 await update.message.reply_text(
            "Вот ссылка на наш официальный сайт:\n"
            "https://www.gov.kz/memleket/entities/mfa-busan"
