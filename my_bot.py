from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = "7568589896:AAF6WNjcbv0JoKujy44DsG3RtAe78JE57pU"
RENDER_URL = "https://telegram-bot-4-my1j.onrender.com"

# Главное меню
LANGUAGE_MENU = [
    [InlineKeyboardButton("Қазақша", callback_data="lang_kz")],
    [InlineKeyboardButton("Русский", callback_data="lang_ru")],
]

KZ_MENU = [
    [InlineKeyboardButton("Консулдық мәселелер", callback_data="kz_consular")],
    [InlineKeyboardButton("Жұмыс уақыты", callback_data="kz_working_hours")],
    [InlineKeyboardButton("Өтініш нысандары", callback_data="kz_forms")],
    [InlineKeyboardButton("Жиі қойылатын сұрақтар", callback_data="kz_faq")],
    [InlineKeyboardButton("Байланыс ақпараты", callback_data="kz_contacts")],
]

RU_MENU = [
    [InlineKeyboardButton("Консульские вопросы", callback_data="ru_consular")],
    [InlineKeyboardButton("Время работы", callback_data="ru_working_hours")],
    [InlineKeyboardButton("Шаблоны заявлений", callback_data="ru_forms")],
    [InlineKeyboardButton("Часто задаваемые вопросы", callback_data="ru_faq")],
    [InlineKeyboardButton("Контакты", callback_data="ru_contacts")],
]

BACK_BUTTON = [
    [InlineKeyboardButton("Назад", callback_data="back")],
]

def start(update: Update, context: CallbackContext):
    user_first_name = update.effective_user.first_name
    greeting = (
        f"Қайырлы күн  / Добрый день, {user_first_name}! Қош келдіңіз/Добро пожаловать!\n"
        "Вас приветствует Генеральное консульство Республики Казахстан в городе Пусан.\n"
        "Чем мы можем вам помочь?"
    )
    update.message.reply_text(
        greeting,
        reply_markup=InlineKeyboardMarkup(LANGUAGE_MENU)
    )

def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    # Меню на казахском языке
    if query.data == "lang_kz":
        query.edit_message_text(
            "Тілді таңдадыңыз: Қазақша",
            reply_markup=InlineKeyboardMarkup(KZ_MENU)
        )

    elif query.data == "kz_contacts":
        text = (
            "Қазақстан Республикасының Пусан қаласындағы Бас Консулдығы (Корея Республикасы)\n"
            "Мекенжай: Пусан қ. 244, Jungang-daero, Dong-gu (48732)\n"
            "Тел: +(82 51) 466 7001, \nКонсулдық бөлім: +(82 51) 469 7003\n"
            "Ресми сайты: https://www.gov.kz/memleket/entities/mfa-busan\n"
            "Орналасқан жері: https://maps.app.goo.gl/AwckvtyLfNTZfjQZ8\n\n"
            "E-mail: busan@mfa.kz"
        )
        query.edit_message_text(
            text,
            reply_markup=InlineKeyboardMarkup(BACK_BUTTON)
        )

    elif query.data == "kz_consular":
        consular_menu = [
            [InlineKeyboardButton("ҚР азаматының паспортын ресімдеу", url="https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181319?directionId=_58636")],
            [InlineKeyboardButton("Шетелде баланың тууын мемлекеттік тіркеу", url="https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181318?directionId=_58636")],
            [InlineKeyboardButton("Назад", callback_data="lang_kz")],
        ]
        query.edit_message_text(
            "Консулдық мәселелер тізімі:",
            reply_markup=InlineKeyboardMarkup(consular_menu)
        )

    elif query.data == "kz_working_hours":
        text = (
            "Жұмыс тәртібі:\n"
            "Келушілерді консулдық мәселелер бойынша қабылдау дүйсенбі, сейсенбі, бейсенбі және жұма күндері сағат 9.30-ден 12.30-ге және 16.00-ден 17.00-ге дейін жүзеге асырылады.\n"
            "Сәрсенбі күні — қабылдамайтын күн.\n"
            "Сенбі және жексенбі күндері, сондай-ақ Қазақстан мереке күндері - демалыс күні."
        )
        query.edit_message_text(
            text,
            reply_markup=InlineKeyboardMarkup(BACK_BUTTON)
        )

    elif query.data == "kz_forms":
        query.edit_message_text(
            "Өтініш нысандарын мына сілтемеден жүктеуге болады: https://www.gov.kz/memleket/entities/mfa-busan/documents/details/753610?lang=kk",
            reply_markup=InlineKeyboardMarkup(BACK_BUTTON)
        )

    # Меню на русском языке
    elif query.data == "lang_ru":
        query.edit_message_text(
            "Вы выбрали язык: Русский",
            reply_markup=InlineKeyboardMarkup(RU_MENU)
        )

    elif query.data == "ru_contacts":
        text = (
            "Генеральное консульство Республики Казахстан в г. Пусан (Республика Корея)\n"
            "Адрес: г. Пусан 244, Jungang-daero, Dong-gu (48732)\n"
            "Тел: +(82 51) 466 7001, \nКонсульский отдел: +(82 51) 469 7003\n"
            "Официальный сайт: https://www.gov.kz/memleket/entities/mfa-busan\n"
            "Местонахождение: https://maps.app.goo.gl/AwckvtyLfNTZfjQZ8\n\n"
            "Эл. Почта: busan@mfa.kz"
        )
        query.edit_message_text(
            text,
            reply_markup=InlineKeyboardMarkup(BACK_BUTTON)
        )

    elif query.data == "back":
        query.edit_message_text(
            "Чем мы можем вам помочь?",
            reply_markup=InlineKeyboardMarkup(LANGUAGE_MENU)
        )

def main():
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button_handler))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
