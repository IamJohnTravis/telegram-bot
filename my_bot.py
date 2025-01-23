from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Токен вашего бота
TOKEN = "7568589896:AAF6WNjcbv0JoKujy44DsG3RtAe78JE57pU"

# Удаление существующего Webhook
bot = Bot(token=TOKEN)
bot.delete_webhook(drop_pending_updates=True)

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Кнопки для выбора языка
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
        ["Бастапқы бетке оралу", "қаз/рус"],
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
        ["Вернуться в главное меню", "қаз/рус"],
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Вы выбрали язык: Русский",
        reply_markup=reply_markup
    )

# Функция для обработки выбора пользователя
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Қазақша":
        await kazakh_menu(update, context)
    elif text == "Русский":
        await russian_menu(update, context)
    elif text == "қаз/рус":
        await start(update, context)
    elif text == "Консулдық мәселелер":
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
            ["Бастапқы бетке оралу", "қаз/рус"],
        ]

        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

        await update.message.reply_text(
            "Консулдық мәселелер туралы толық ақпарат: https://www.gov.kz/memleket/entities/mfa-busan/activities/58636?lang=ru",
            reply_markup=reply_markup
        )
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
    elif text == "Жұмыс уақыты":
        await update.message.reply_text(
            "Жұмыс тәртібі:\n"
            "Келушілерді консулдық мәселелер бойынша қабылдау дүйсенбі, сейсенбі, бейсенбі және жұма күндері сағат 9.30-ден 12.30-ге және 16.00-ден 17.00-ге дейін жүзеге асырылады.\n"
            "Сәрсенбі күні — қабылдамайтын күн.\n"
            "Сенбі және жексенбі күндері, сондай-ақ Қазақстан мереке күндері - демалыс күні."
        )
    elif text == "Өтініш нысандары":
        await update.message.reply_text(
            "Өтініш нысандарын мына сілтемеден жүктеуге болады: https://www.gov.kz/memleket/entities/mfa-busan/documents/details/753610?lang=kk",
            reply_markup=ReplyKeyboardMarkup([["Бастапқы бетке оралу", "қаз/рус"]], resize_keyboard=True)
        )
    elif text == "Байланыс ақпараты":
        await update.message.reply_text(
            "Қазақстан Республикасының Пусан қаласындағы Бас Консулдығы (Корея Республикасы)\n"
            "Мекенжай: Пусан қ. 244, Jungang-daero, Dong-gu (48732)\n"
            "Тел: +(82 51) 466 7001, \nКонсулдық бөлім: +(82 51) 469 7003\n"
            "Ресми сайты: https://www.gov.kz/memleket/entities/mfa-busan\n"
            "Орналасқан жері: https://maps.app.goo.gl/AwckvtyLfNTZfjQZ8\n"
            "https://naver.me/5wW6EhBY\n"
            "E-mail: busan@mfa.kz",
            reply_markup=ReplyKeyboardMarkup([["Бастапқы бетке оралу", "қаз/рус"]], resize_keyboard=True)
        )
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
            ["Вернуться в главное меню", "қаз/рус"],
        ]

        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

        await update.message.reply_text(
            "Консульские вопросы: https://www.gov.kz/memleket/entities/mfa-busan/activities/58636?lang=ru",
            reply_markup=reply_markup
        )
    elif text == "Время работы":
        await update.message.reply_text(
            "Прием посетителей по консульским вопросам осуществляется в понедельник, вторник, четверг и пятницу с 9.30 до 12.30 ч., выдача готовых документов с 16.00 до 17.00 ч.\n"
            "Среда — неприемный день.\n"
            "Суббота, воскресенье, а также праздничные дни Казахстана — выходные дни.\n"
            "Прием осуществляется по живой очереди"
        )
    elif text == "Шаблоны заявлений":
        await update.message.reply_text(
            "Шаблоны заявлений можно найти по ссылке: https://www.gov.kz/memleket/entities/mfa-busan/documents/details/753610?lang=ru",
            reply_markup=ReplyKeyboardMarkup([["Вернуться в главное меню", "қаз/рус"]], resize_keyboard=True)
        )
    elif text == "Контакты":
        await update.message.reply_text(
            "Генеральное консульство Республики Казахстан в г. Пусан (Республика Корея):\n"
            "Адрес: г. Пусан 244, Jungang-daero, Dong-gu (48732)\n"
            "Тел: +(82 51) 466 7001, \nКонсульский отдел: +(82 51) 469 7003\n"
            "Официальный сайт: https://www.gov.kz/memleket/entities/mfa-busan\n"
            "Местонахождение: https://maps.app.goo.gl/AwckvtyLfNTZfjQZ8\n"
            "https://naver.me/5wW6EhBY\n"
            "Эл. Почта: busan@mfa.kz",
            reply_markup=ReplyKeyboardMarkup([["Вернуться в главное меню", "қаз/рус"]], resize_keyboard=True)
        )
    elif text == "Оформление паспорта гражданина РК":
        await update.message.reply_text("Информация: https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181319?directionId=_58637")
    elif text == "Государственная регистрация рождения ребенка за рубежом":
        await update.message.reply_text("Информация: https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181318?directionId=_58637")
    elif text == "Государственная регистрация заключения брака":
        await update.message.reply_text("Информация: https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181311?directionId=_58637")
    elif text == "Государственная регистрация расторжения брака за рубежом":
        await update.message.reply_text("Информация: https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181316?directionId=_58637")
    elif text == "Государственная регистрация смерти за рубежом":
        await update.message.reply_text("Информация: https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181314?directionId=_58637")
    elif text == "Оформление свидетельства на возвращение в РК":
        await update.message.reply_text("Информация: https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181317?directionId=_58637")
    elif text == "Оформление разрешения на ПМЖ за рубежом":
        await update.message.reply_text("Информация: https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181315?directionId=_58637")
    elif text == "Выдача повторных свидетельств и справок":
        await update.message.reply_text("Информация: https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181313?directionId=_58637")
    elif text == "Консульский учет":
        await update.message.reply_text("Информация: https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181310?directionId=_58637")
    elif text == "Вернуться в главное меню":
        await russian_menu(update, context)
    elif text == "Бастапқы бетке оралу":
        await kazakh_menu(update, context)
    else:
        await update.message.reply_text("Пожалуйста, выберите одну из доступных опций.")

# Основной блок для запуска бота
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен! Нажмите Ctrl+C для остановки.")
    app.run_polling()
