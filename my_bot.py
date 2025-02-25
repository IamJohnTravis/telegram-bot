import requests
import threading
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import time

# Токен вашего бота
TOKEN = "7568589896:AAF6WNjcbv0JoKujy44DsG3RtAe78JE57pU"

# Ссылка для восстановления сервиса
RENDER_RESTART_URL = "https://api.render.com/deploy/srv-cu8tv3i3esus739soco0?key=1ITZYdIhpPI"

#добавьте свою ссылку
SERVICE_URL = "https://your-service-url.com"

# Функция для проверки доступности сервиса
def check_service():
    try:
        response = requests.get(SERVICE_URL, timeout=5)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"⚠️ Ошибка проверки сервиса: {e}")
        return False

# Функция для восстановления сервиса
def restart_service():
    try:
        response = requests.get(RENDER_RESTART_URL)
        if response.status_code == 200:
            print("✅ Сервис перезапущен.")
        else:
            print(f"⚠️ Ошибка: {response.status_code}")
    except requests.RequestException as e:
        print(f"🚨 Не удалось перезапустить сервис: {e}")

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Қазақша", "Русский"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text(
        f"Қайырлы күн / Добрый день, {update.effective_user.first_name}!\n"
        "Вас приветствует Генеральное консульство РК в Пусане.\n"
        "Выберите язык / Тілді таңдаңыз:",
        reply_markup=reply_markup
    )

# Функция для отображения меню на казахском языке
async def kazakh_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Консулдық мәселелер", "Жұмыс уақыты"],
        ["Өтініш нысандары", "Жиі қойылатын сұрақтар"],
        ["Байланыс ақпараты", "🔙 Бастапқы бетке"],
    ]
    await update.message.reply_text("Сіз Қазақ тілін таңдадыңыз.", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

# Функция для отображения меню на русском языке
async def russian_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Консульские вопросы", "Время работы"],
        ["Шаблоны заявлений", "Часто задаваемые вопросы"],
        ["Контакты", "🔙 Вернуться назад"],
    ]
    await update.message.reply_text("Вы выбрали Русский язык.", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

#новая функция для отправления ссылок
async def send_info(update: Update, text: str, url: str = None):
    message = text
    if url:
        message += f"\nПодробнее: {url}"
    await update.message.reply_text(message)
    
# Функция для обработки выбора пользователя
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    menu_options = {
    "Қазақша": kazakh_menu,
    "Русский": russian_menu,
    "қаз/рус": start,
    "Консулдық мәселелер": lambda u, c: send_info(
        u, "Консулдық мәселелер туралы толық ақпарат:", "https://www.gov.kz/memleket/entities/mfa-busan/activities/58636?lang=ru"
    ),
    "ҚР азаматының паспортын ресімдеу": lambda u, c: send_info(
        u, "Информация:", "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181319?directionId=_58636"
    ),
    "Шетелде баланың тууын мемлекеттік тіркеу": lambda u, c: send_info(
        u, "Информация:", "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181318?directionId=_58636"
    ),
    "Шетелде неке қиюды мемлекеттік тіркеу": lambda u, c: send_info(
        u, "Информация:", "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181311?directionId=_58636"
    ),
    "Шетелде некені бұзуды мемлекеттік тіркеу": lambda u, c: send_info(
        u, "Информация:", "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181316?directionId=_58636"
    ),
    "Шетелде қайтыс болуды мемлекеттік тіркеу": lambda u, c: send_info(
        u, "Информация:", "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181314?directionId=_58636"
    ),
    "ҚР-ге оралуға арналған куәлікті ресімдеу": lambda u, c: send_info(
        u, "Информация:", "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181317?directionId=_58636"
    ),
    "Қазақстаннан тыс жерде тұрақты тұруға рұқсат алу": lambda u, c: send_info(
        u, "Информация:", "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181315?directionId=_58636"
    ),
    "Қайталама куәліктер мен анықтамаларды есепке алу": lambda u, c: send_info(
        u, "Информация:", "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181313?directionId=_58636"
    ),
    "Консулдық есеп": lambda u, c: send_info(
        u, "Информация:", "https://www.gov.kz/memleket/entities/mfa-busan/press/article/details/181310?directionId=_58636"
    ),
    "Жұмыс уақыты": lambda u, c: send_info(
        u,
        "Жұмыс тәртібі:\nКелушілерді консулдық мәселелер бойынша қабылдау дүйсенбі, сейсенбі, бейсенбі және жұма күндері сағат 9.30-ден 12.30-ге және 16.00-ден 17.00-ге дейін жүзеге асырылады.\nСәрсенбі күні — қабылдамайтын күн.\nСенбі және жексенбі күндері, сондай-ақ Қазақстан мереке күндері - демалыс күні."
    ),
    "Өтініш нысандары": lambda u, c: send_info(
        u, "Өтініш нысандарын мына сілтемеден жүктеуге болады:", "https://www.gov.kz/memleket/entities/mfa-busan/documents/details/753610?lang=kk"
    ),
    "Байланыс ақпараты": lambda u, c: send_info(
        u,
        "Қазақстан Республикасының Пусан қаласындағы Бас Консулдығы (Корея Республикасы)\nМекенжай: Пусан қ. 244, Jungang-daero, Dong-gu (48732)\nТел: +(82 51) 466 7001, \nКонсулдық бөлім: +(82 51) 469 7003\nРесми сайты: https://www.gov.kz/memleket/entities/mfa-busan\nОрналасқан жері: https://maps.app.goo.gl/AwckvtyLfNTZfjQZ8\nhttps://naver.me/5wW6EhBY\nE-mail: busan@mfa.kz"
    ),
    "Бастапқы бетке оралу": kazakh_menu,
    "Вернуться в главное меню": russian_menu,
}

    
    if text in menu_options:
        await menu_options[text](update, context)
    else:
        await update.message.reply_text("Пожалуйста, выберите одну из доступных опций.")

def monitor_service():
    while True:
        if not check_service():
            print("⛔️ Сервис недоступен. Перезапускаю...")
            restart_service()
        time.sleep(300)
        
# Основной блок для запуска бота
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    threading.Thread(target=monitor_service, daemon=True).start()
    print("🤖 Бот запущен! Нажмите Ctrl+C для остановки.")
    app.run_polling()
