from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from config import TOKEN
from cities import CITIES

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [[city] for city in CITIES.keys()]
    markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    await update.message.reply_text("Shaharni tanlang:", reply_markup=markup)

# Shahar nomiga javob
async def handle_city(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = update.message.text
    if city in CITIES:
        times = CITIES[city]
        msg = f"{city} namoz vaqtlari:\n"
        for key, val in times.items():
            msg += f"{key}: {val}\n"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
    else:
        await update.message.reply_text("Iltimos, shahar nomini tugmalar orqali tanlang.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_city))
    app.run_polling()
