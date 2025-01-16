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
        )
