from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Токен вашего бота
TOKEN = "7568589896:AAF6WNjcbv0JoKujy44DsG3RtAe78JE57pU"

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Кнопки для главного меню
    keyboard = [
        ["1 Часто задаваемые вопросы"],  # Первая строка кнопок
        ["2 Контакты"],  # Вторая строка кнопок
        ["3 Назад в главное меню"],  # Третья строка кнопок
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

# Функция для раздела "Часто задаваемые вопросы"
async def show_faq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Кнопки для раздела "Часто задаваемые вопросы"
    keyboard = [
        ["Паспорт"],  # Первая строка кнопок
        ["Регистрация рождения ребенка"],  # Вторая строка кнопок
        ["Регистрация брака"],  # Третья строка кнопок
        ["Назад в главное меню"],  # Кнопка для возврата в главное меню
    ]

    # Создаём клавиатуру
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    # Отправляем сообщение с кнопками
    await update.message.reply_text(
        "Вы выбрали 'Часто задаваемые вопросы'. Пожалуйста, выберите интересующий вас пункт:",
        reply_markup=reply_markup
    )

# Функция для обработки выбора пользователя
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "1 Часто задаваемые вопросы":
        await show_faq(update, context)  # Переходим в раздел FAQ
    elif text == "2 Контакты":
        # Отправляем ссылку на официальный сайт
        await update.message.reply_text(
            "Вот ссылка на наш официальный сайт:\n"
            "https://www.gov.kz/memleket/entities/mfa-busan\n\n"
            "Генеральное консульство Республики Казахстан в г. Пусан (Республика Корея):\n"
            "Адрес: г. Пусан 244, Jungang-daero, Dong-gu (48732)\n"
            "Тел: +(82 51) 466 7001, Консульский отдел: +(82 51) 469 7003\n"
            "Эл. Почта: busan@mfa.kz\n\n"
            "Режим работы:\n"
            "Прием посетителей по консульским вопросам осуществляется в понедельник, вторник, четверг и пятницу с 9.30 до 12.30 ч., выдача готовых документов с 16.00 до 17.00 ч.\n"
            "Среда — неприемный день.\n"
            "Суббота, воскресенье, а также праздничные дни Казахстана — выходные дни."
        )
    elif text == "Паспорт":
        await update.message.reply_text(
            "Информация о паспорте: ... (добавьте нужный текст)"
        )
    elif text == "Регистрация рождения ребенка":
        await update.message.reply_text("Информация о регистрации рождения ребенка: ... (добавьте нужный текст)")
    elif text == "Регистрация брака":
        await update.message.reply_text("Информация о регистрации брака: ... (добавьте нужный текст)")
    elif text == "Назад в главное меню":
        await start(update, context)  # Возвращаемся к главному меню
    else:
        await update.message.reply_text("Пожалуйста, выберите одну из доступных опций.")

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
