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
    elif text == "Консулдық мәселелер":
        await kazakh_consular_issues(update, context)
    elif text == "Консульские вопросы":
        await russian_consular_issues(update, context)
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

# Функции для казахского меню
async def kazakh_contact_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Бастапқы бетке оралу"]]
    await update.message.reply_text(
        "Қазақстан Республикасының Пусан қаласындағы Бас Консулдығы (Корея Республикасы)\n"
        "Мекенжай: Пусан қ. 244, Jungang-daero, Dong-gu (48732)\n"
        "Тел: +(82 51) 466 7001, \n"
        "Консулдық бөлім: +(82 51) 469 7003\n"
        "E-mail: busan@mfa.kz",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

async def kazakh_working_hours(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Бастапқы бетке оралу"]]
    await update.message.reply_text(
        "Жұмыс тәртібі:\n"
        "Келушілерді консулдық мәселелер бойынша қабылдау дүйсенбі, сейсенбі, бейсенбі және жұма күндері сағат 9.30-ден 12.30-ге және 16.00-ден 17.00-ге дейін жүзеге асырылады.\n"
        "Сәрсенбі күні — қабылдамайтын күн.\n"
        "Сенбі және жексенбі күндері, сондай-ақ Қазақстан мереке күндері - демалыс күні.",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

async def kazakh_consular_issues(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Бастапқы бетке оралу"]]
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
    response = "Консулдық мәселелер бойынша сілтемелер:\n"
    for issue, link in links.items():
        response += f"{issue}: {link}\n"
    await update.message.reply_text(response, reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

# Функции для русского меню
async def russian_contact_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
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

async def russian_working_hours(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Вернуться в главное меню"]]
    await update.message.reply_text(
        "Прием посетителей по консульским вопросам осуществляется в понедельник, вторник, четверг и пятницу с 9.30 до 12.30 ч., выдача готовых документов с 16.00 до 17.00 ч.\n"
        "Среда — неприемный день.\n"
        "Суббота, воскресенье, а также праздничные дни Казахстана — выходные дни.",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

async def russian_consular_issues(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Вернуться в главное меню"]]
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
    response = "Ссылки по консульским вопросам:\n"
    for issue, link in links.items():
        response += f"{issue}: {link}\n"
    await update.message.reply_text
    
