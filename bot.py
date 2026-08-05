from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

from config import TOKEN, ADMIN_ID
from database import add_user, get_balance
from admin import admin
from settings import (
    REFERRAL_BONUS,
    TASK_REWARD,
    MIN_WITHDRAW,
    WITHDRAW_METHOD,
)

menu = [
    ["💰 Balance", "👥 Referral"],
    ["📋 Task", "📤 Withdraw"],
    ["ℹ️ Help"],
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    add_user(update.effective_user.id)

    keyboard = ReplyKeyboardMarkup(menu, resize_keyboard=True)

    text = f"""
👋 Welcome {update.effective_user.first_name}!

🎉 Welcome to DailyEasyEarnFBInsta

Choose an option from the menu below.
"""

    await update.message.reply_text(
        text,
        reply_markup=keyboard
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text

    if msg == "💰 Balance":
        balance = get_balance(update.effective_user.id)
        await update.message.reply_text(
            f"💰 Balance: ${balance:.2f} USD"
        )

    elif msg == "👥 Referral":
        await update.message.reply_text(
            f"👥 Your Referral Link:\n"
            f"https://t.me/FBInstaEasyEarnBot?start={update.effective_user.id}\n\n"
            f"🎁 Referral Bonus: ${REFERRAL_BONUS:.2f} USDT"
        )

    elif msg == "📋 Task":
    await update.message.reply_text(
        f"📋 Task Reward: ${TASK_REWARD:.2f} USDT"
   ) 

    elif msg == "📤 Withdraw":
        balance = get_balance(update.effective_user.id)

        if balance < MIN_WITHDRAW:
            await update.message.reply_text(
                f"❌ Minimum Withdraw: ${MIN_WITHDRAW:.2f}\n"
                f"💰 Your Balance: ${balance:.2f}"
            )
        else:
            await update.message.reply_text(
                f"💳 Withdraw Method: {WITHDRAW_METHOD}\n\n"
                "Send your wallet address to continue."
            )

    elif msg == "ℹ️ Help":
        await update.message.reply_text(
            "Need help? Contact Admin."
        )
async def admin_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "ref_bonus":
        await query.message.reply_text(
            f"👥 Current Referral Bonus: ${REFERRAL_BONUS:.2f} USDT"
        )

    elif query.data == "task_reward":
        await query.message.reply_text(
            f"🎯 Current Task Reward: ${TASK_REWARD:.2f} USDT"
        )

    elif query.data == "min_withdraw":
        await query.message.reply_text(
            f"💸 Minimum Withdraw: ${MIN_WITHDRAW:.2f} via {WITHDRAW_METHOD}"
        )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("admin", admin))
app.add_handler(CallbackQueryHandler(admin_buttons))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))

print("Bot is running...")
app.run_polling()