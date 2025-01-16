from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Токен вашего бота
TOKEN = "7568589896:AAF6WNjcbv0JoKujy44DsG3RtAe78JE57pU"

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Привет, {update.effective_user.first_name}! Добро пожаловать! 🎉\n"
        "Чем я могу вам помочь?"
    )

# Основной блок для запуска бота
if __name__ == "__main__":
    # Создание приложения
    app = ApplicationBuilder().token(TOKEN).build()

    # Добавление обработчика команды /start
    app.add_handler(CommandHandler("start", start))

    print("Бот запущен! Нажмите Ctrl+C для остановки.")
    # Запуск бота
    app.run_polling()
