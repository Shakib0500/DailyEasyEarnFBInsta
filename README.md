# DailyEasyEarnFBInsta
Telegram Earn Bot
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# এখানে আপনার BotFather থেকে পাওয়া Token বসান
TOKEN = "8970530045:AAGyLP-wR6C8sc8tMDdm07K4qPTSGLUc9og"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is working!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("এই Bot সফলভাবে চলছে।")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
