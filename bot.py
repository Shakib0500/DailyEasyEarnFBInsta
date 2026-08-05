from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters, CallbackQueryHandler
from admin import admin
from database import get_balance

TOKEN = "8970530045:AAGyLP-wR6C8sc8tMDdm07K4qPTSGLUc9og"

menu = [
    ["💰 Balance", "👥 Referral"],
    ["🎁 Daily Bonus", "📤 Withdraw"],
    ["ℹ️ Help"]
]

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text

    if msg == "💰 Balance":
        balance = get_balance(update.effective_user.id)
        await update.message.reply_text(f"💰 Balance: ${balance:.2f} USD")

    elif msg == "👥 Referral":
        await update.message.reply_text(
            "👥 Your Referral Link:\nhttps://t.me/@FBInstaEasyEarnBot?start=" 
            + str(update.effective_user.id)
        )

    elif msg == "🎁 Daily Bonus":
        await update.message.reply_text("🎁 Daily Bonus feature is coming soon.")

    elif msg == "📤 Withdraw":
        await update.message.reply_text("📤 Withdraw feature is coming soon.")

    elif msg == "ℹ️ Help":
        await update.message.reply_text("Need help? Contact Admin.")