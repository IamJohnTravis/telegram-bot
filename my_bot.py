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

# Функция для меню на русском языке
async def russian_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Контакты"],
        ["Консульские вопросы"],
        ["Время работы"],
        ["Шаблоны заявлений"],
        ["Вернуться в главное меню"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Вы выбрали Русский язык. Пожалуйста, выберите пункт меню:", reply_markup=reply_markup)

# Функция для "Контакты"
async def contact_info_russian(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Вернуться в главное меню"]]
    await update.message.reply_text(
        "Генеральное консульство Республики Казахстан в г. Пусан (Республика Корея)\n"
        "Адрес: г. Пусан 244, Jungang-daero, Dong-gu (48732)\n"
        "Тел: +(82 51) 466 7001, \n"
        "Консульский отдел: +(82 51) 469 7003\n"
        "Эл. Почта: busan@mfa.kz\n"
        "Официальный сайт: https://www.gov.kz/memleket/entities/mfa-busan?lang=ru",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

# Функция для "Консульские вопросы"
async def consular_issues_russian(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
        ["Вернуться в главное меню"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Список консульских вопросов:", reply_markup=reply_markup)

# Функция для обработки выбора консульских вопросов
async def handle_consular_issues_russian(update: Update, context: ContextTypes.DEFAULT_TYPE):
    links = {
        "Оформление паспорта гражданина РК": "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181319?directionId=_58637",
        "Государственная регистрация рождения ребенка за рубежом": "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181318?directionId=_58637",
        "Государственная регистрация заключения брака": "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181311?directionId=_58637",
        "Государственная регистрация расторжения брака за рубежом": "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181316?directionId=_58637",
        "Государственная регистрация смерти за рубежом": "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181314?directionId=_58637",
        "Оформление свидетельства на возвращение в РК": "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181317?directionId=_58637",
        "Оформление разрешения на ПМЖ за рубежом": "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181315?directionId=_58637",
        "Выдача повторных свидетельств и справок": "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181313?directionId=_58637",
        "Консульский учет": "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181310?directionId=_58637"
    }
    text = update.message.text
    if text in links:
        await update.message.reply_text(f"Подробнее по ссылке: {links[text]}", reply_markup=ReplyKeyboardMarkup([["Вернуться в главное меню"]], resize_keyboard=True))
    elif text == "Вернуться в главное меню":
        await russian_menu(update, context)

# Функция для "Время работы"
async def working_hours_russian(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Вернуться в главное меню"]]
    await update.message.reply_text(
        "Прием посетителей по консульским вопросам осуществляется в понедельник, вторник, четверг и пятницу с 9.30 до 12.30 ч., выдача готовых документов с 16.00 до 17.00 ч.\n"
        "Среда — неприемный день.\n"
        "Суббота, воскресенье, а также праздничные дни Казахстана — выходные дни.",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

# Функция для "Шаблоны заявлений"
async def forms_russian(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Вернуться в главное меню"]]
    await update.message.reply_text(
        "Шаблоны заявлений доступны по ссылке:\n"
        "https://www.gov.kz/memleket/entities/mfa-busan/documents/details/753610?lang=ru",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

# Функция для обработки выбора пользователя
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Қазақша":
        await kazakh_menu(update, context)
    elif text == "Русский":
        await russian_menu(update, context)
    elif text == "Байланыс ақпараты":
        await contact_info(update, context)
    elif text == "Контакты":
        await contact_info_russian(update, context)
    elif text == "Консулдық мәселелер":
        await consular_issues(update, context)
    elif text == "Консульские вопросы":
        await consular_issues_russian(update, context)
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
        "Бастапқы бетке оралу"
    ]:
        await handle_consular
