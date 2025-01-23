from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Токен вашего бота
TOKEN = "7568589896:AAF6WNjcbv0JoKujy44DsG3RtAe78JE57pU"

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Қазақша", "Русский"],
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

    await update.message.reply_text(
        f"Қайырлы күн  / Добрый день, {update.effective_user.first_name}! Қош келдіңіз/Добро пожаловать! \n"
        "Вас приветствует Генеральное консульство Республики Казахстан в городе Пусан.\n"
        "Чем мы можем вам помочь?",
        reply_markup=reply_markup
    )

# Функция для отображения меню на казахском языке
async def kazakh_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Консулдық мәселелер"],
        ["Жұмыс уақыты"],
        ["Өтініш нысандары"],
        ["Жиі қойылатын сұрақтар"],
        ["Байланыс ақпараты"],
        ["Назад"],
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Тілді таңдадыңыз: Қазақша",
        reply_markup=reply_markup
    )

# Функция для отображения меню на русском языке
async def russian_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Консульские вопросы"],
        ["Время работы"],
        ["Шаблоны заявлений"],
        ["Часто задаваемые вопросы"],
        ["Контакты"],
        ["Назад"],
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Вы выбрали язык: Русский",
        reply_markup=reply_markup
    )

# Функция для отображения меню "Консулдық мәселелер"
async def konsuldyk_maseleler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["ҚР азаматының паспортын ресімдеу"],
        ["Шетелде баланың тууын мемлекеттік тіркеу"],
        ["Шетелде неке қиюды мемлекеттік тіркеу"],
        ["Шетелде некені бұзуды мемлекеттік тіркеу"],
        ["Шетелде қайтыс болуды мемлекеттік тіркеу"],
        ["ҚР-ге оралуға арналған куәлікті ресімдеу"],
        ["Қазақстаннан тыс жерде тұрақты тұруға рұқсат алу"],
        ["Қайталама куәліктер мен анықтамаларды есепке алу"],
        ["Консулдық есеп"],
        ["Назад"],
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Консулдық мәселелер туралы толық ақпарат: https://www.gov.kz/memleket/entities/mfa-busan/activities/58636?lang=ru",
        reply_markup=reply_markup
    )

# Функция для обработки выбора пользователя
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Қазақша":
        await kazakh_menu(update, context)
    elif text == "Русский":
        await russian_menu(update, context)
    elif text == "Консулдық мәселелер":
        await konsuldyk_maseleler(update, context)
    elif text == "ҚР азаматының паспортын ресімдеу":
        await update.message.reply_text(
            "Информация: https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181319?directionId=_58636"
        )
    elif text == "Шетелде баланың тууын мемлекеттік тіркеу":
        await update.message.reply_text(
            "Информация: https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181318?directionId=_58636"
        )
    elif text == "Шетелде неке қиюды мемлекеттік тіркеу":
        await update.message.reply_text(
            "Информация: https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181311?directionId=_58636"
        )
    elif text == "Шетелде некені бұзуды мемлекеттік тіркеу":
        await update.message.reply_text(
            "Информация: https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181316?directionId=_58636"
        )
    elif text == "Шетелде қайтыс болуды мемлекеттік тіркеу":
        await update.message.reply_text(
            "Информация: https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181314?directionId=_58636"
        )
    elif text == "ҚР-ге оралуға арналған куәлікті ресімдеу":
        await update.message.reply_text(
            "Информация: https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181317?directionId=_58636"
        )
    elif text == "Қазақстаннан тыс жерде тұрақты тұруға рұқсат алу":
        await update.message.reply_text(
            "Информация: https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181315?directionId=_58636"
        )
    elif text == "Қайталама куәліктер мен анықтамаларды есепке алу":
        await update.message.reply_text(
            "Информация: https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181313?directionId=_58636"
        )
    elif text == "Консулдық есеп":
        await update.message.reply_text(
            "Информация: https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181310?directionId=_58636"
        )
    elif text == "Назад":
        await start(update, context)
    elif text == "Консульские вопросы":
        keyboard = [
            ["Оформление паспорта гражданина РК"],
            ["Государственная регистрация рождения ребенка за рубежом"],
            ["Государственная регистрация заключения брака"],
            ["Государственная регистрация расторжения брака за рубежом"],
            ["Государственная регистрация смерти за рубежом"],
            ["Оформление свидетельства на возвращение в РК"],
            ["Оформление разрешения на ПМЖ за рубежом"],
            ["Выдача повторных свидетельств и справок"],
            ["Консульский учет"],
            ["Назад"],
        ]

        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

        await update.message.reply_text(
            "Консульские вопросы: https://www.gov.kz/memleket/entities/mfa-busan/activities/58636?lang=ru",
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text("Пожалуйста, выберите одну из доступных опций.")

# Основной блок для запуска бота
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен! Нажмите Ctrl+C для остановки.")
    app.run_polling()
