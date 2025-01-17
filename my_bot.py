from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7568589896:AAF6WNjcbv0JoKujy44DsG3RtAe78JE57pU"

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


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.effective_user.first_name
    greeting = (
        f"Қайырлы күн  / Добрый день, {user_first_name}! Қош келдіңіз/Добро пожаловать!\n"
        "Вас приветствует Генеральное консульство Республики Казахстан в городе Пусан.\n"
        "Чем мы можем вам помочь?"
    )
    await update.message.reply_text(
        greeting,
        reply_markup=InlineKeyboardMarkup(LANGUAGE_MENU),
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "lang_kz":
        await query.edit_message_text(
            "Тілді таңдадыңыз: Қазақша",
            reply_markup=InlineKeyboardMarkup(KZ_MENU),
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
        await query.edit_message_text(
            text,
            reply_markup=InlineKeyboardMarkup(BACK_BUTTON),
        )

    elif query.data == "lang_ru":
        await query.edit_message_text(
            "Вы выбрали язык: Русский",
            reply_markup=InlineKeyboardMarkup(RU_MENU),
        )

    elif query.data == "back":
        await query.edit_message_text(
            "Чем мы можем вам помочь?",
            reply_markup=InlineKeyboardMarkup(LANGUAGE_MENU),
        )


def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    application.run_polling()


if __name__ == "__main__":
    main()
