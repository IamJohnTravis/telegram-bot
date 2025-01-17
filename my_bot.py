from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Токен вашего бота
TOKEN = "7568589896:AAF6WNjcbv0JoKujy44DsG3RtAe78JE57pU"

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Кнопки для выбора языка
    keyboard = [
        ["Қазақша", "Русский"]  # Две кнопки для выбора языка
    ]

    # Создаём клавиатуру
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    # Отправляем сообщение с кнопками
    await update.message.reply_text(
        f"Қайырлы күн/Добрый день, {update.effective_user.first_name}! Қош келдіңіз/Добро пожаловать! "
        "Вас приветствует Генеральное консульство Республики Казахстан в городе Пусан.\n"
        "Чем мы можем вам помочь?",
        reply_markup=reply_markup
    )

# Функция для меню на казахском языке
async def kazakh_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Байланыс ақпараты"],
        ["Консулдық мәселелер"],
        ["Жұмыс уақыты"],
        ["Өтініш нысандары"],
        ["Бастапқы бетке оралу"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Сіз Қазақ тілін таңдадыңыз. Төмендегі мәзірден таңдаңыз:", reply_markup=reply_markup)

# Функция для "Байланыс ақпараты"
async def contact_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Вернуться меню"]]
    await update.message.reply_text(
        "Қазақстан Республикасының Пусан қаласындағы Бас Консулдығы (Корея Республикасы)\n"
        "Мекенжай: Пусан қ. 244, Jungang-daero, Dong-gu (48732)\n"
        "Тел: +(82 51) 466 7001, \n"
        "Консулдық бөлім: +(82 51) 469 7003\n"
        "E-mail: busan@mfa.kz",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

# Функция для "Консулдық мәселелер"
async def consular_issues(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
        ["Вернуться меню"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Консулдық мәселелер тізімі:", reply_markup=reply_markup)

# Функция для обработки выбора консулдық мәселелер
async def handle_consular_issues(update: Update, context: ContextTypes.DEFAULT_TYPE):
    links = {
        "ҚР азаматының паспортын ресімдеу": "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181319?directionId=_58636",
        "Шетелде баланың тууын мемлекеттік тіркеу": "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181318?directionId=_58636",
        "Шетелде неке қиюды мемлекеттік тіркеу": "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181311?directionId=_58636",
        "Шетелде некені бұзуды мемлекеттік тіркеу": "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181316?directionId=_58636",
        "Шетелде қайтыс болуды мемлекеттік тіркеу": "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181314?directionId=_58636",
        "ҚР-ге оралуға арналған куәлікті ресімдеу": "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181317?directionId=_58636",
        "Қазақстаннан тыс жерде тұрақты тұруға рұқсат алу": "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181315?directionId=_58636",
        "Қайталама куәліктер мен анықтамаларды есепке алу": "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181313?directionId=_58636",
        "Консулдық есеп": "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181310?directionId=_58636"
    }
    text = update.message.text
    if text in links:
        await update.message.reply_text(f"Толығырақ мына сілтемеден көріңіз: {links[text]}", reply_markup=ReplyKeyboardMarkup([["Вернуться меню"]], resize_keyboard=True))
    elif text == "Вернуться меню":
        await kazakh_menu(update, context)

# Функция для "Жұмыс уақыты"
async def working_hours(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Вернуться меню"]]
    await update.message.reply_text(
        "Жұмыс тәртібі:\n"
        "Келушілерді консулдық мәселелер бойынша қабылдау дүйсенбі, сейсенбі, бейсенбі және жұма күндері сағат 9.30-ден 12.30-ге және 16.00-ден 17.00-ге дейін жүзеге асырылады.\n"
        "Сәрсенбі күні — қабылдамайтын күн.\n"
        "Сенбі және жексенбі күндері, сондай-ақ Қазақстан мереке күндері - демалыс күні.",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

# Функция для "Өтініш нысандары"
async def forms(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Вернуться меню"]]
    await update.message.reply_text(
        "Өтініш нысандарын мына жерден жүктей аласыз:\n"
        "https://www.gov.kz/memleket/entities/mfa-busan/documents/details/753610?lang=kk",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

# Функция для обработки выбора пользователя
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Қазақша":
        await kazakh_menu(update, context)
    elif text == "Байланыс ақпараты":
        await contact_info(update, context)
    elif text == "Консулдық мәселелер":
        await consular_issues(update, context)
    elif text in [
        "ҚР азаматының паспортын ресімдеу",
        "Шетелде баланың тууын мемлекеттік тіркеу",
        "Шетелде неке қиюды мемлекеттік тіркеу",
        "Шетелде некені бұзуды мемлекеттік тіркеу",
        "Шетелде қайтыс болуды мемлекеттік тіркеу",
        "ҚР-ге оралуға арналған куәлікті ресімдеу",
        "Қазақстаннан тыс жерде тұрақты тұруға рұқсат алу",
        "Қайталама куәліктер мен анықтамаларды есепке алу",
        "Консулдық есеп",
        "Вернуться меню"
    ]:
        await handle_consular_issues(update, context)
    elif text == "Жұмыс уақыты":
        await working_hours(update, context)
    elif text == "Өтініш нысандары":
        await forms(update, context)
    elif text == "Вернуться меню":
        await start(update, context)

# Основной блок для запуска бота
if __name__ == "__main__":
    # Создание приложения
    app = ApplicationBuilder().token(TOKEN).build()

    # Добавляем обработчики команд и сообщений
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен! Нажмите Ctrl+C для остановки.")
    # Запуск бота
    app.run_polling()
