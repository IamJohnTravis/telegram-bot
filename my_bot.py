from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "ВАШ_ТОКЕН"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["1 Часто задаваемые вопросы"], ["2 Контакты"], ["3 Назад в главное меню"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        f"Добрый день, {update.effective_user.first_name}! Добро пожаловать!",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "1 Часто задаваемые вопросы":
        await update.message.reply_text("Это раздел часто задаваемых вопросов.")
    elif text == "2 Контакты":
        await update.message.reply_text("Наш сайт: https://www.gov.kz/memleket/entities/mfa-busan")
    elif text == "3 Назад в главное меню":
        await start(update, context)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
