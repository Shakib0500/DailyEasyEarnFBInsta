from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from admin import admin
from telegram.ext import CallbackQueryHandler

TOKEN = "8970530045:AAGyLP-wR6C8sc8tMDdm07K4qPTSGLUc9og"

menu = [
    ["💰 Balance", "👥 Referral"],
    ["🎁 Daily Bonus", "📤 Withdraw"],
    ["ℹ️ Help"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup(menu, resize_keyboard=True)

    text = f"""
👋 Welcome {update.effective_user.first_name}!

🎉 Welcome to DailyEasyEarnFBInsta

Choose an option from the menu below.
"""

    await update.message.reply_text(text, reply_markup=keyboard)

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text

    if msg == "💰 Balance":
        await update.message.reply_text(f"💰 Balance: ${balance:.2f} USD")

    elif msg == "👥 Referral":
        await update.message.reply_text("👥 Your Referral Link:\nhttps://t.me/@FBInstaEasyEarnBot?start=" + str(update.effective_user.id))

    elif msg == "🎁 Daily Bonus":
        await update.message.reply_text("🎁 Daily Bonus feature is coming soon.")

    elif msg == "📤 Withdraw":
        await update.message.reply_text("📤 Withdraw feature is coming soon.")

    elif msg == "ℹ️ Help":
        await update.message.reply_text("Need help? Contact Admin.")
async def admin_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "ref_bonus":
        await query.message.reply_text("👥 Current Referral Bonus: 0.01 USDT")

    elif query.data == "task_reward":
        await query.message.reply_text("🎯 Current Task Reward: 0.01 USDT")

    elif query.data == "min_withdraw":
        await query.message.reply_text("💸 Minimum Withdraw: 0.20 USDT")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("admin", admin))
app.add_handler(CallbackQueryHandler(admin_buttons))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))

print("Bot is running...")
app.run_polling()
