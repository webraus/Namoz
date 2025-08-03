from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
from config import TOKEN
from cities import CITIES

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    keyboard = [[city] for city in CITIES.keys()]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await context.bot.send_message(chat_id=chat_id, text="Shaharni tanlang:", reply_markup=reply_markup)

async def send_prayer_times(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = update.message.text
    if city in CITIES:
        times = CITIES[city]
        msg = f"{city} namoz vaqtlari:
"
        for key, val in times.items():
            msg += f"{key}: {val}\n"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Shahar topilmadi.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_prayer_times))
    print("Bot ishga tushdi.")
    app.run_polling()

if __name__ == "__main__":
    main()
