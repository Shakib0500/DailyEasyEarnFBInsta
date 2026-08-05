from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8970530045:AAGyLP-wR6C8sc8tMDdm07K4qPTSGLUc9og"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is working!")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
